#!/usr/bin/env python3
import json
import os
import sys
import argparse
from pathlib import Path

def patch_json(file_path, patches):
    if not file_path.exists():
        print(f"File not found: {file_path}")
        return False

    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        for key, value in patches.items():
            keys = key.split('.')
            d = data
            for k in keys[:-1]:
                if k not in d:
                    d[k] = {}
                d = d[k]
            d[keys[-1]] = value

        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully patched {file_path}")
        return True
    except Exception as e:
        print(f"Error patching {file_path}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Σ_APΩ₂ Identity Injector")
    parser.add_argument("--path", required=True, help="Path to the app source root")
    parser.add_argument("--name", required=True, help="Short name of the app")
    parser.add_argument("--long-name", help="Long name of the app")
    parser.add_argument("--bundle-id", required=True, help="Darwin bundle identifier")
    parser.add_argument("--author", default="alpha_prime_omega", help="App author")

    args = parser.parse_args()
    root = Path(args.path)

    # Define patches for VS Code style projects
    product_patches = {
        "nameShort": args.name,
        "nameLong": args.long_name or args.name,
        "applicationName": args.name.lower().replace(" ", "-"),
        "darwinBundleIdentifier": args.bundle_id,
        "crashReporter.companyName": args.author,
        "crashReporter.productName": args.name
    }

    package_patches = {
        "name": args.name.lower().replace(" ", "-"),
        "displayName": args.name,
        "author": args.author,
        "description": f"Sovereign Application: {args.name} | Built by {args.author}"
    }

    print(f"💉 Injecting identity: {args.name} ({args.bundle_id})")

    success = True
    success &= patch_json(root / "product.json", product_patches)
    success &= patch_json(root / "package.json", package_patches)

    if success:
        print("✅ Identity injection complete.")
    else:
        print("❌ Identity injection failed for some components.")

if __name__ == "__main__":
    main()
