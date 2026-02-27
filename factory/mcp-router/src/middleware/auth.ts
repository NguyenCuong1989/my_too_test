import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';
import admin from 'firebase-admin';
import logger from '../utils/logger.js';

const JWT_SECRET = process.env.JWT_SECRET || 'super-secret-mcp-key';

// Initialize Firebase Admin
if (!admin.apps.length) {
  admin.initializeApp({
    projectId: process.env.GOOGLE_CLOUD_PROJECT || 'gen-lang-client-0863690953'
  });
}

const db = admin.firestore();

export const authenticateJWT = (req: Request, res: Response, next: NextFunction) => {
  const authHeader = req.headers['authorization'];

  if (authHeader) {
    const token = typeof authHeader === 'string' ? authHeader.split(' ')[1] : undefined;

    if (!token) {
        logger.warn('Token missing from authorization header');
        res.sendStatus(401);
        return;
    }

    jwt.verify(token, JWT_SECRET, (err: any, user: any) => {
      if (err) {
        logger.warn({ err }, 'Invalid JWT token attempt');
        return res.sendStatus(403);
      }

      (req as any).user = user;
      next();
    });
  } else {
    logger.warn('Missing authorization header');
    res.sendStatus(401);
  }
};

export const checkBillingStatus = async (req: Request, res: Response, next: NextFunction) => {
  const user = (req as any).user;
  if (!user || !user.uid) {
    logger.warn('Billing check failed: User context missing');
    return res.sendStatus(401);
  }

  try {
    const userDoc = await db.collection('users').doc(user.uid).get();

    if (!userDoc.exists) {
      logger.warn({ userId: user.uid }, 'Billing check failed: User not found in Firestore');
      return res.status(402).json({ error: 'Subscription required' });
    }

    const data = userDoc.data();
    const subscription = data?.subscription;
    const billing = data?.billing;

    if (!subscription || subscription.status !== 'active') {
      logger.warn({ userId: user.uid, status: subscription?.status }, 'Billing check failed: Inactive subscription');
      return res.status(402).json({ error: 'Active subscription required' });
    }

    if (!billing || billing.quota_remaining <= 0) {
      logger.warn({ userId: user.uid }, 'Billing check failed: Quota exhausted');
      return res.status(429).json({ error: 'Quota exhausted' });
    }

    // Attach billing info to request for later use (e.g. decrementing)
    (req as any).billing = billing;
    next();
  } catch (err) {
    logger.error({ err, userId: user.uid }, 'Error checking billing status');
    res.sendStatus(500);
  }
};

export const generateToken = (payload: object) => {
  return jwt.sign(payload, JWT_SECRET, { expiresIn: '24h' });
};
