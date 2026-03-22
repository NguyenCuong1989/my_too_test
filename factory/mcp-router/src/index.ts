import express from 'express';
import admin from 'firebase-admin';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import { z } from 'zod';
import logger from './utils/logger.js';
import { authenticateJWT, checkBillingStatus } from './middleware/auth.js';

const app = express();
app.use(express.json());

const db = admin.firestore();

// 1. Health Monitoring Endpoint (Hardened with Firestore check)
app.get('/health', async (req, res) => {
  try {
    // Check Firestore connectivity
    await db.collection('health_check').doc('pulse').set({
      last_seen: admin.firestore.FieldValue.serverTimestamp()
    });
    res.status(200).json({
      status: 'ok',
      database: 'connected',
      timestamp: new Date().toISOString()
    });
  } catch (err: any) {
    logger.error({ err }, 'Health check failed - Database disconnected');
    res.status(503).json({
      status: 'error',
      database: 'disconnected',
      error: err.message
    });
  }
});

// 2. Internal MCP Logic (example tool)
const server = new McpServer({
  name: "SovereignRouter",
  version: "1.1.0"
});

server.tool(
  "calculate-harmony",
  "Calculates system synergy score",
  {
    component: z.string().describe("Component name to evaluate"),
  },
  async ({ component }) => {
    logger.info({ component }, 'Executing harmony calculation');
    return {
      content: [{ type: "text", text: `Harmony score for ${component} is 0.98` }]
    };
  }
);

// 3. Authorized Tool Execution Layer (External)
app.post('/execute', authenticateJWT, checkBillingStatus, async (req, res) => {
  const { tool, arguments: args, idempotency_key } = req.body as any;
  const user = (req as any).user;
  const billing = (req as any).billing;
  const requestId = crypto.randomUUID(); // For correlation

  if (!idempotency_key) {
    return res.status(400).json({ error: 'idempotency_key is required for RIL compliance' });
  }

  logger.info({ requestId, tool, args, userId: user.uid, idempotency_key }, 'Authorized tool execution request');

  try {
    const logRef = db.collection('execution_logs').doc(idempotency_key);

    // 1. IDEMPOTENCY CHECK (Replay Logic)
    const existingLog = await logRef.get();
    if (existingLog.exists) {
      logger.info({ requestId, idempotency_key }, 'Replaying existing result (Idempotency Hit)');
      return res.json(existingLog.data()?.result);
    }

    // 2. PERFORM TASK EXECUTION (Placeholder for ACE Worker call)
    // For now, we simulate a successful execution of the hardened SLI Skill
    const mockResult = {
      version: "1.0.1",
      seal: "mock_seal_for_demo",
      data: { status: "success", result: "Enriched data for " + (args?.company_name || 'unknown') },
      metadata: { execution_time: new Date().toISOString(), determinism_score: 1.0 }
    };

    // 3. ATOMIC TRANSACTION: Decrement Quota + Store Log
    const userRef = db.collection('users').doc(user.uid);

    await db.runTransaction(async (tx) => {
      const userDoc = await tx.get(userRef);
      if (!userDoc.exists) throw new Error('User not found');

      const currentQuota = userDoc.data()?.billing?.quota_remaining || 0;
      if (currentQuota <= 0) throw new Error('Quota exhausted during execution');

      // Update User Quota
      tx.update(userRef, {
        'billing.quota_remaining': admin.firestore.FieldValue.increment(-1),
        'subscription.updated': admin.firestore.FieldValue.serverTimestamp()
      });

      // Secure the execution log for idempotency (7-day TTL proposed)
      const expiresAt = new Date();
      expiresAt.setDate(expiresAt.getDate() + 7);

      tx.set(logRef, {
        user_id: user.uid,
        tool,
        args,
        result: mockResult,
        created_at: admin.firestore.FieldValue.serverTimestamp(),
        expires_at: admin.firestore.Timestamp.fromDate(expiresAt),
        request_id: requestId
      });
    });

    logger.info({ requestId, tool, userId: user.uid }, 'Tool execution success and quota decremented');
    res.json(mockResult);

  } catch (err: any) {
    logger.error({ requestId, err, userId: user.uid }, 'Error during tool execution or RIL enforcement');
    res.status(500).json({ error: err.message || 'Internal server error' });
  }
});

// 4. Server Start
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  logger.info(`MCP Router hardened and listening on port ${PORT}`);
});
