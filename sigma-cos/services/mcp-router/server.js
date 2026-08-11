// mcp-router — Node.js / Express
// Simple request router. Validates JWT, dispatches to registered services or external connectors.
import express from "express";
import http from "node:http";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { readFileSync } from "node:fs";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PORT = Number(process.env.PORT || 3000);
const SECRET = process.env.SIGMA_SECRET || "dev-secret-change-me";

// ---- shared auth (Node port of common/auth.py, kept in sync) ----
import crypto from "node:crypto";

function b64url(b) { return Buffer.from(b).toString("base64url"); }
function b64urlDecode(s) { return Buffer.from(s, "base64url"); }

function issueToken(sub, constraints = { max_objects: 100, max_arrays: 50, max_depth: 10 }) {
  const header = { alg: "HS256", typ: "JWT" };
  const now = Math.floor(Date.now() / 1000);
  const payload = { sub, constraints, iat: now, exp: now + 86400 };
  const h = b64url(JSON.stringify(header));
  const p = b64url(JSON.stringify(payload));
  const sig = b64url(crypto.createHmac("sha256", SECRET).update(`${h}.${p}`).digest());
  return `${h}.${p}.${sig}`;
}

function verifyToken(token) {
  if (!token || token.split(".").length !== 3) throw new Error("malformed");
  const [h, p, s] = token.split(".");
  const expected = b64url(crypto.createHmac("sha256", SECRET).update(`${h}.${p}`).digest());
  if (!crypto.timingSafeEqual(Buffer.from(s), Buffer.from(expected))) throw new Error("bad sig");
  const payload = JSON.parse(b64urlDecode(p).toString());
  if (Math.floor(Date.now() / 1000) >= payload.exp) throw new Error("expired");
  return payload;
}

// ---- service registry ----
const SERVICES = {
  "factory-worker": { host: process.env.FACTORY_HOST || "factory-worker", port: Number(process.env.FACTORY_PORT || 8080) },
  "ai-sidecar":     { host: process.env.AI_HOST     || "ai-sidecar",     port: Number(process.env.AI_PORT     || 8000) },
  "firebase-emu":   { host: process.env.FIREBASE_HOST|| "firebase-emulator", port: Number(process.env.FIREBASE_PORT || 4400) },
};

// ---- connector catalog (external integrations) ----
const CONNECTORS = {
  asana:  { base: process.env.ASANA_BASE  || "https://app.asana.com/api/1.0", auth: process.env.ASANA_PAT  || "" },
  google: { base: process.env.GOOGLE_BASE || "https://www.googleapis.com",     auth: process.env.GOOGLE_TOKEN || "" },
  gpt:    { base: process.env.GPT_BASE    || "https://api.openai.com/v1",      auth: process.env.OPENAI_API_KEY || "" },
  github: { base: process.env.GITHUB_BASE || "https://api.github.com",         auth: process.env.GITHUB_TOKEN || "" },
};

// ---- helpers ----
function proxy(target, path, method, body, extraHeaders = {}) {
  return new Promise((resolve) => {
    const s = SERVICES[target];
    if (!s) return resolve({ status: 404, body: { error: `unknown service: ${target}` } });
    const data = body ? JSON.stringify(body) : null;
    const req = http.request({ host: s.host, port: s.port, path, method,
      headers: { "Content-Type": "application/json", "Content-Length": data ? Buffer.byteLength(data) : 0, ...extraHeaders } },
      (res) => {
        let buf = "";
        res.on("data", (c) => buf += c);
        res.on("end", () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(buf || "{}") }); }
          catch { resolve({ status: res.statusCode, body: { raw: buf } }); }
        });
      });
    req.on("error", (e) => resolve({ status: 0, body: { error: e.message } }));
    if (data) req.write(data);
    req.end();
  });
}

function callConnector(name, path, method, body) {
  return new Promise((resolve) => {
    const c = CONNECTORS[name];
    if (!c) return resolve({ status: 404, body: { error: `unknown connector: ${name}` } });
    if (!c.auth) return resolve({ status: 503, body: { error: `${name} connector not configured (missing env var)` } });
    const data = body ? JSON.stringify(body) : null;
    const url = new URL(c.base + path);
    const req = http.request({ host: url.hostname, port: url.port || 443, path: url.pathname + url.search, method,
      headers: { "Content-Type": "application/json", "Authorization": `Bearer ${c.auth}`, "Content-Length": data ? Buffer.byteLength(data) : 0 } },
      (res) => {
        let buf = "";
        res.on("data", (c) => buf += c);
        res.on("end", () => {
          try { resolve({ status: res.statusCode, body: JSON.parse(buf || "{}") }); }
          catch { resolve({ status: res.statusCode, body: { raw: buf } }); }
        });
      });
    req.on("error", (e) => resolve({ status: 0, body: { error: e.message } }));
    if (data) req.write(data);
    req.end();
  });
}

// ---- express app ----
const app = express();
app.use(express.json({ limit: "1mb" }));

app.get("/health", (_req, res) => res.json({ ok: true, service: "mcp-router", services: Object.keys(SERVICES), connectors: Object.keys(CONNECTORS) }));

app.post("/auth/token", (req, res) => {
  const { subject, constraints } = req.body || {};
  if (!subject) return res.status(400).json({ error: "subject required" });
  res.json({ token: issueToken(subject, constraints), service: "mcp-router" });
});

// proxy to internal services
app.post("/call/:target", async (req, res) => {
  const token = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  try { verifyToken(token); } catch (e) { return res.status(401).json({ error: "auth", detail: e.message }); }
  const { path = "/", method = "GET", body } = req.body || {};
  const out = await proxy(req.params.target, path, method, body, {
    "Authorization": `Bearer ${token}`,
    "X-Source-Service": "mcp-router",
  });
  res.status(out.status || 502).json(out.body);
});

// external connector call
app.post("/connector/:name", async (req, res) => {
  const token = (req.headers.authorization || "").replace(/^Bearer\s+/i, "");
  try { verifyToken(token); } catch (e) { return res.status(401).json({ error: "auth", detail: e.message }); }
  const { path = "/", method = "GET", body } = req.body || {};
  const out = await callConnector(req.params.name, path, method, body);
  res.status(out.status || 502).json(out.body);
});

// health-check all internal services
app.get("/health/all", async (_req, res) => {
  const results = {};
  for (const [name, s] of Object.entries(SERVICES)) {
    const out = await proxy(name, "/health", "GET", null);
    results[name] = { status: out.status, ...out.body };
  }
  res.json({ ok: true, services: results, connectors: CONNECTORS });
});

app.listen(PORT, "0.0.0.0", () => console.log(`[mcp-router] listening on :${PORT}`));