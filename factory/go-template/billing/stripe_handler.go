package billing

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"

	"cloud.google.com/go/firestore"
	"github.com/labstack/echo/v4"
	"github.com/stripe/stripe-go/v78"
	"github.com/stripe/stripe-go/v78/webhook"
	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
)

type StripeHandler struct {
	Firestore *firestore.Client
}

func NewStripeHandler(db *firestore.Client) *StripeHandler {
	return &StripeHandler{Firestore: db}
}

func (h *StripeHandler) HandleWebhook(c echo.Context) error {
	const MaxBodyBytes = int64(65536)
	payload, err := io.ReadAll(io.LimitReader(c.Request().Body, MaxBodyBytes))
	if err != nil {
		return c.String(http.StatusBadRequest, "Error reading request body")
	}

	sigHeader := c.Request().Header.Get("Stripe-Signature")
	endpointSecret := os.Getenv("STRIPE_WEBHOOK_SECRET")

	event, err := webhook.ConstructEvent(payload, sigHeader, endpointSecret)
	if err != nil {
		log.Printf("⚠️ Webhook signature verification failed: %v", err)
		return c.String(http.StatusBadRequest, "Invalid signature")
	}

	// 1. Idempotency Check using Firestore Transaction
	eventRef := h.Firestore.Collection("stripe_events").Doc(event.ID)

	err = h.Firestore.RunTransaction(c.Request().Context(), func(ctx context.Context, tx *firestore.Transaction) error {
		_, err := tx.Get(eventRef)
		if err == nil {
			return fmt.Errorf("event already processed: %s", event.ID)
		}
		if status.Code(err) != codes.NotFound {
			return err
		}

		// Handle events
		switch event.Type {
		case "checkout.session.completed":
			var session stripe.CheckoutSession
			if err := json.Unmarshal(event.Data.Raw, &session); err != nil {
				return err
			}
			if err := h.handleCheckoutCompletedTx(ctx, tx, &session); err != nil {
				return err
			}
		case "invoice.payment_failed":
			var invoice stripe.Invoice
			if err := json.Unmarshal(event.Data.Raw, &invoice); err != nil {
				return err
			}
			if err := h.handlePaymentFailedTx(ctx, tx, &invoice); err != nil {
				return err
			}
		case "customer.subscription.deleted":
			var sub stripe.Subscription
			if err := json.Unmarshal(event.Data.Raw, &sub); err != nil {
				return err
			}
			if err := h.handleSubscriptionDeletedTx(ctx, tx, &sub); err != nil {
				return err
			}
		}

		// Log processed event
		return tx.Set(eventRef, map[string]interface{}{
			"processed_at": firestore.ServerTimestamp,
			"type":         event.Type,
			"status":       "success",
		})
	})

	if err != nil {
		log.Printf("⚠️ Webhook processing skipped or failed: %v", err)
		return c.JSON(http.StatusOK, map[string]string{"status": "skipped", "reason": err.Error()})
	}

	return c.JSON(http.StatusOK, map[string]string{"status": "received"})
}

func (h *StripeHandler) handleCheckoutCompletedTx(ctx context.Context, tx *firestore.Transaction, session *stripe.CheckoutSession) error {
	userID := session.Metadata["user_id"]
	if userID == "" {
		return fmt.Errorf("no user_id in session metadata")
	}

	plan := "basic"
	quotaLimit := 100

	// Price ID Mapping (should be from env)
	priceID := ""
	if session.Subscription != nil && session.Subscription.Items != nil && len(session.Subscription.Items.Data) > 0 {
		priceID = session.Subscription.Items.Data[0].Price.ID
	} else if session.LineItems != nil && len(session.LineItems.Data) > 0 {
		priceID = session.LineItems.Data[0].Price.ID
	}

	if priceID == os.Getenv("STRIPE_PRICE_PRO") {
		plan = "pro"
		quotaLimit = 1000
	}

	userRef := h.Firestore.Collection("users").Doc(userID)
	updates := map[string]interface{}{
		"identity.stripe_customer_id": session.Customer.ID,
		"subscription": map[string]interface{}{
			"status": "active",
			"plan":   plan,
			"updated": firestore.ServerTimestamp,
		},
		"billing": map[string]interface{}{
			"quota_limit":     quotaLimit,
			"quota_remaining": quotaLimit,
			"last_reset":      firestore.ServerTimestamp,
		},
	}

	return tx.Set(userRef, updates, firestore.MergeAll)
}

func (h *StripeHandler) handlePaymentFailedTx(ctx context.Context, tx *firestore.Transaction, invoice *stripe.Invoice) error {
	if invoice.Customer == nil {
		return nil
	}

	// Find user by customer ID
	users := h.Firestore.Collection("users").Where("identity.stripe_customer_id", "==", invoice.Customer.ID).Limit(1).Documents(ctx)
	doc, err := users.Next()
	if err != nil {
		return nil // User not found, nothing to update
	}

	return tx.Update(doc.Ref, []firestore.Update{
		{Path: "subscription.status", Value: "past_due"},
		{Path: "subscription.updated", Value: firestore.ServerTimestamp},
	})
}

func (h *StripeHandler) handleSubscriptionDeletedTx(ctx context.Context, tx *firestore.Transaction, sub *stripe.Subscription) error {
	if sub.Customer == nil {
		return nil
	}

	users := h.Firestore.Collection("users").Where("identity.stripe_customer_id", "==", sub.Customer.ID).Limit(1).Documents(ctx)
	doc, err := users.Next()
	if err != nil {
		return nil
	}

	return tx.Update(doc.Ref, []firestore.Update{
		{Path: "subscription.status", Value: "canceled"},
		{Path: "subscription.updated", Value: firestore.ServerTimestamp},
	})
}

// IsNotFound is a helper to check firestore/grpc errors
func IsNotFound(err error) bool {
	return status.Code(err) == codes.NotFound
}
