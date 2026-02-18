# Mobile Control Spec (Status: COMPLETE)

## Role
- Acts as control plane only; never executes UI actions.
- Issues lifecycle commands: start, pause, resume, stop, kill.
- Displays status, logs, STOP reasons (read-only).

## Trust Level
- Semi-trusted UI; cannot bypass policy; all commands re-validated on device.

## Data Flow
1. Human selects intent or approves pending command.
2. Mobile app sends signed request to device-bound AnLenh.
3. Decision Core validates policy + state; either executes or denies with reason.

## Constraints
- No Accessibility (AX) access from mobile.
- No input emission from mobile.
- Network channel treated untrusted; signatures + device binding required.

## Platforms
- iOS native client
- Web control UI (same capabilities, browser-based)
