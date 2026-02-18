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

IDENTITY="IDENTITY_NOT_FOUND"
ENTITLEMENTS="entitlements/AXCONTROL.entitlements"
APP_BUNDLE="build/AXCONTROL.app"
ZIP_BUNDLE="build/AXCONTROL.zip"

if [[ "${IDENTITY}" == "IDENTITY_NOT_FOUND" ]]; then
  echo "ABORT: No Developer ID Application identity present."
  echo "STATUS: ARMED / WAITING_FOR_IDENTITY"
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
