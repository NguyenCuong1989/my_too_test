# AXCONTROL UI (Local)

Single-user UI (admin/admin) acting purely as renderer + input collector. No logic, no policy, no executor. Communicates with core via Snapshot JSON contract (see CONTRACT.md).

## Run
cd ui/client
npm install
npm run dev

## Notes
- Use admin/admin to enter.
- Ensure core snapshot HTTP bridge is running (R-22) before using.
- No cloud calls; local-only.
