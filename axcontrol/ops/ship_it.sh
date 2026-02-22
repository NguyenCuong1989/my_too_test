# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a closed Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> COG -> Projection(Π) -> Artifact
#
# =============================================================================
set -euo pipefail

echo "=== AXCONTROL :: SOVEREIGN SIGNING RITUAL ==="

IDENTITY="${IDENTITY_OVERRIDE:-IDENTITY_NOT_FOUND}"
ENTITLEMENTS="entitlements/AXCONTROL.entitlements"
APP_BUNDLE="build/AXCONTROL.app"
ZIP_BUNDLE="build/AXCONTROL.zip"

echo "[PRECHECK] Running no-drift invariants..."
if [[ "${SKIP_INVARIANT_TESTS:-0}" != "1" ]]; then
  AXCONTROL_SIM=1 python3 -m unittest tests.test_bridge_no_drift -v
else
  echo "[PRECHECK] SKIP_INVARIANT_TESTS=1 set; skipping invariant tests."
fi

# auto-discover Developer ID Application if not provided
FOUND_ID=""
if command -v security >/dev/null 2>&1; then
  set +o pipefail
  FOUND_ID=$(security find-identity -p codesigning -v 2>/dev/null | grep "Developer ID Application" | head -n1 | sed 's/^[^"]*"//;s/".*$//' || true)
  set -o pipefail
fi

if [[ "${IDENTITY}" == "IDENTITY_NOT_FOUND" ]]; then
  IDENTITY="${FOUND_ID}"
fi

if [[ -z "${IDENTITY}" ]]; then
  echo "ABORT: No valid Developer ID Application found."
  echo "STATUS: ID_NOT_FOUND / ARMED"
  exit 1
fi

if [[ ! -d "${APP_BUNDLE}" ]]; then
  echo "ABORT: app bundle '${APP_BUNDLE}' not found. Build before signing."
  exit 1
fi

if [[ ! -f "${ENTITLEMENTS}" ]]; then
  echo "ABORT: entitlements file '${ENTITLEMENTS}' missing."
  exit 1
fi

echo "[1/4] Signing embedded binaries (runtime, libs, tools)..."
find "${APP_BUNDLE}/Contents/Resources" -type f \\( -name \"*.so\" -o -name \"*.dylib\" -o -perm +111 \\) -print -exec codesign --force --sign \"${IDENTITY}\" {} \\;

echo "[2/4] Signing launcher with entitlements..."
codesign --force --options runtime --entitlements \"${ENTITLEMENTS}\" --sign \"${IDENTITY}\" \"${APP_BUNDLE}/Contents/MacOS/AXCONTROL\"

echo "[3/4] Sealing bundle..."
codesign --force --options runtime --entitlements \"${ENTITLEMENTS}\" --deep --sign \"${IDENTITY}\" \"${APP_BUNDLE}\"

echo "[4/4] Notarize + staple..."
ditto -c -k --keepParent \"${APP_BUNDLE}\" \"${ZIP_BUNDLE}\"
xcrun notarytool submit \"${ZIP_BUNDLE}\" --keychain-profile \"AC_PASSWORD\" --wait
xcrun stapler staple \"${APP_BUNDLE}\"

echo \"DONE: AXCONTROL is signed + notarized.\"
