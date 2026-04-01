# core/safety

Safety primitives: kill-switch, stop reasons, and determinism hashing. Human override always wins; kill-switch is local-only and offline-capable.

Stop reasons include vision mismatch, UI state drift, policy denial, permission loss, timing violation, human abort, kill-switch, text-edit blocked (e.g., Notes editor), AX loss, and app switch during guarded navigation.
