package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/signal"
	"syscall"
	"time"

	"cloud.google.com/go/firestore"
	"github.com/NguyenCuong1989/go-factory-template/billing"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

// ProductInfo defines the standardized product metadata
type ProductInfo struct {
	Name    string `json:"name"`
	Version string `json:"version"`
	Status  string `json:"status"`
}

var currentProduct = ProductInfo{
	Name:    "DAIOF Unified Product",
	Version: "v1.0.0",
	Status:  "Operational",
}

func main() {
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	e.Use(middleware.CORS())

	// Firestore Initialization
	ctx := context.Background()
	projectID := os.Getenv("GOOGLE_CLOUD_PROJECT")
	if projectID == "" {
		projectID = "gen-lang-client-0863690953"
	}

	db, err := firestore.NewClient(ctx, projectID)
	if err != nil {
		log.Printf("⚠️ Failed to create Firestore client: %v", err)
	} else {
		billingHandler := billing.NewStripeHandler(db)
		e.POST("/api/webhook/stripe", billingHandler.HandleWebhook)
		log.Printf("💳 Stripe Webhook handler registered at /api/webhook/stripe")
	}

	// Routes
	e.GET("/", handleInfo)
	e.GET("/health", handleHealth)
	e.POST("/mcp", handleMCP)

	// Server management
	go func() {
		port := os.Getenv("PORT")
		if port == "" {
			port = "8080"
		}
		if err := e.Start(":" + port); err != nil && err != http.ErrServerClosed {
			e.Logger.Fatal("shutting down the server")
		}
	}()

	// Graceful shutdown
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt, syscall.SIGTERM)
	<-quit

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	if db != nil {
		db.Close()
	}

	if err := e.Shutdown(ctx); err != nil {
		e.Logger.Fatal(err)
	}
}

func handleInfo(c echo.Context) error {
	return c.JSON(http.StatusOK, currentProduct)
}

func handleHealth(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]string{"status": "UP", "timestamp": time.Now().Format(time.RFC3339)})
}

// MCPRequest represents a minimal Model Context Protocol request
type MCPRequest struct {
	Method string          `json:"method"`
	Params json.RawMessage `json:"params"`
	ID     string          `json:"id"`
}

// MCPResponse represents a minimal Model Context Protocol response
type MCPResponse struct {
	JSONRPC string      `json:"jsonrpc"`
	Result  interface{} `json:"result,omitempty"`
	Error   interface{} `json:"error,omitempty"`
	ID      string      `json:"id"`
}

func handleMCP(c echo.Context) error {
	var req MCPRequest
	if err := c.Bind(&req); err != nil {
		return c.JSON(http.StatusBadRequest, MCPResponse{JSONRPC: "2.0", Error: "Invalid Request", ID: "null"})
	}

	// Dynamic capability mesh routing logic would go here
	log.Printf("[MCP] Method: %s called", req.Method)

	result := map[string]string{
		"message": fmt.Sprintf("Executed %s via Unified Factory Core", req.Method),
	}

	return c.JSON(http.StatusOK, MCPResponse{
		JSONRPC: "2.0",
		Result:  result,
		ID:      req.ID,
	})
}
