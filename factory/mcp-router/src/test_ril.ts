/**
 * REPLAY INTEGRITY LAYER (RIL) - SIMULATION TEST 🧪🛡️
 * Verifies that duplicate requests with the same idempotency_key:
 * 1. Return the cached result (Replay).
 * 2. ONLY decrement quota ONCE.
 */

import admin from 'firebase-admin';

// Initialize Firebase (Assuming service account or ADC is available)
if (!admin.apps.length) {
    admin.initializeApp({
        projectId: process.env.GOOGLE_CLOUD_PROJECT || 'gen-lang-client-0863690953'
    });
}

const db = admin.firestore();

async function simulateExecution(userId, tool, idempotencyKey) {
    console.log(`\n--- 🌀 SIMULATING EXECUTION [Key: ${idempotencyKey}] ---`);
    const logRef = db.collection('execution_logs').doc(idempotencyKey);
    const userRef = db.collection('users').doc(userId);

    try {
        const result = await db.runTransaction(async (tx) => {
            // 1. Check Idempotency
            const existingLog = await tx.get(logRef);
            if (existingLog.exists) {
                console.log("➡️ IDEMPOTENCY HIT: Replaying result.");
                return { replayed: true, result: existingLog.data().result };
            }

            // 2. Business Logic Execution (Simplified)
            console.log("⚡ FIRST EXECUTION: Calculating result...");
            const mockResult = { status: "success", seal: "hash_v1_" + idempotencyKey };

            // 3. Quota Enforcement
            const userDoc = await tx.get(userRef);
            if (!userDoc.exists) throw new Error("User not found");
            const quota = userDoc.data()?.billing?.quota_remaining || 0;
            if (quota <= 0) throw new Error("Quota exhausted");

            // 4. Update State
            tx.update(userRef, { 'billing.quota_remaining': admin.firestore.FieldValue.increment(-1) });
            tx.set(logRef, {
                user_id: userId,
                tool,
                result: mockResult,
                created_at: admin.firestore.FieldValue.serverTimestamp()
            });

            return { replayed: false, result: mockResult };
        });

        return result;
    } catch (err) {
        console.error("❌ Transaction Failed:", err.message);
        throw err;
    }
}

async function runTest() {
    const TEST_USER = "test-user-ril-01";
    const TEST_KEY = "test-idemp-" + Date.now();

    // Ensure test user has quota
    await db.collection('users').doc(TEST_USER).set({
        email: "test@sli.ai",
        billing: { quota_remaining: 10 }
    }, { merge: true });

    console.log("🚀 STARTING RIL DOUBLE-REQUEST AUDIT...");

    // First run
    const res1 = await simulateExecution(TEST_USER, "sli-enrichment", TEST_KEY);
    console.log("Res 1 - Replayed:", res1.replayed, "Seal:", res1.result.seal);

    // Second run (Simulation of network retry)
    const res2 = await simulateExecution(TEST_USER, "sli-enrichment", TEST_KEY);
    console.log("Res 2 - Replayed:", res2.replayed, "Seal:", res2.result.seal);

    // Verify Quota
    const finalDoc = await db.collection('users').doc(TEST_USER).get();
    const finalQuota = finalDoc.data()?.billing?.quota_remaining;
    console.log(`\n📊 FINAL AUDIT: Quota Remaining: ${finalQuota}`);

    if (res2.replayed && finalQuota === 9) {
        console.log("\n✅ RIL VERIFICATION PASSED: Double-request safe. Zero drift detected.");
    } else {
        console.log("\n❌ RIL VERIFICATION FAILED: Logic drift or double-charge occurred.");
    }
}

runTest().catch(console.error);
