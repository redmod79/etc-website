#!/usr/bin/env python3
"""
merge_versions.py -- Pre-build script for ETC website version toggle.

Scans docs/studies/*/v2/ for versioned content. For each file that exists in
both the study root and v2/, creates a merged file wrapping both versions in
<div class="version-content" data-version="v1|v2"> blocks.

Run BEFORE mkdocs build:
  cd D:/bible/etc-website
  python merge_versions.py
  mkdocs build

To undo (restore originals):
  python merge_versions.py --restore
"""

import argparse
import os
import sys

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
STUDIES_DIR = os.path.join(DOCS_DIR, "studies")
BACKUP_SUFFIX = "_v1_backup"
MERGEABLE_FILES = [
    "conclusion-simple.md",
    "CONCLUSION.md",
    "03-analysis.md",
    "02-verses.md",
    "04-word-studies.md",
    "01-topics.md",
    "PROMPT.md",
]


def find_v2_studies():
    """Find all study directories that have a v2/ subdirectory."""
    results = []
    if not os.path.isdir(STUDIES_DIR):
        return results
    for name in sorted(os.listdir(STUDIES_DIR)):
        study_dir = os.path.join(STUDIES_DIR, name)
        v2_dir = os.path.join(study_dir, "v2")
        if os.path.isdir(v2_dir):
            results.append((name, study_dir, v2_dir))
    return results


def merge_file(v1_path, v2_path, output_path):
    """Create a merged file with version-togglable content blocks."""
    with open(v1_path, "r", encoding="utf-8") as f:
        v1_content = f.read()
    with open(v2_path, "r", encoding="utf-8") as f:
        v2_content = f.read()

    merged = (
        '<div class="version-content" data-version="v1" markdown="1">\n\n'
        f"{v1_content}\n\n"
        "</div>\n\n"
        '<div class="version-content" data-version="v2" markdown="1">\n\n'
        f"{v2_content}\n\n"
        "</div>\n"
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(merged)


def cmd_merge(args):
    studies = find_v2_studies()
    if not studies:
        print("No v2/ directories found. Nothing to merge.")
        return

    total_merged = 0
    for name, study_dir, v2_dir in studies:
        merged_count = 0
        backup_dir = os.path.join(study_dir, BACKUP_SUFFIX)

        for fname in MERGEABLE_FILES:
            v1_file = os.path.join(study_dir, fname)
            v2_file = os.path.join(v2_dir, fname)

            if not os.path.exists(v1_file) or not os.path.exists(v2_file):
                continue

            # Skip if already merged (check for version-content marker)
            with open(v1_file, "r", encoding="utf-8") as f:
                first_line = f.readline()
            if 'class="version-content"' in first_line:
                continue

            # Backup original
            os.makedirs(backup_dir, exist_ok=True)
            backup_path = os.path.join(backup_dir, fname)
            if not os.path.exists(backup_path):
                with open(v1_file, "r", encoding="utf-8") as src:
                    with open(backup_path, "w", encoding="utf-8") as dst:
                        dst.write(src.read())

            merge_file(v1_file, v2_file, v1_file)
            merged_count += 1

        if merged_count > 0:
            print(f"  {name}: merged {merged_count} file(s)")
            total_merged += merged_count

    # Also merge master-evidence.md if v2 exists
    master_v1 = os.path.join(DOCS_DIR, "master-evidence.md")
    master_v2 = os.path.join(DOCS_DIR, "master-evidence-v2.md")
    if os.path.exists(master_v1) and os.path.exists(master_v2):
        with open(master_v1, "r", encoding="utf-8") as f:
            first_line = f.readline()
        if 'class="version-content"' not in first_line:
            backup = os.path.join(DOCS_DIR, "master-evidence" + BACKUP_SUFFIX + ".md")
            if not os.path.exists(backup):
                with open(master_v1, "r", encoding="utf-8") as src:
                    with open(backup, "w", encoding="utf-8") as dst:
                        dst.write(src.read())
            merge_file(master_v1, master_v2, master_v1)
            print(f"  master-evidence.md: merged")
            total_merged += 1

    print(f"\nTotal: {total_merged} file(s) merged.")


def cmd_restore(args):
    studies = find_v2_studies()
    restored = 0

    for name, study_dir, _ in studies:
        backup_dir = os.path.join(study_dir, BACKUP_SUFFIX)
        if not os.path.isdir(backup_dir):
            continue

        for fname in os.listdir(backup_dir):
            backup_path = os.path.join(backup_dir, fname)
            original_path = os.path.join(study_dir, fname)
            with open(backup_path, "r", encoding="utf-8") as src:
                with open(original_path, "w", encoding="utf-8") as dst:
                    dst.write(src.read())
            restored += 1

    # Restore master-evidence.md
    master_backup = os.path.join(DOCS_DIR, "master-evidence" + BACKUP_SUFFIX + ".md")
    if os.path.exists(master_backup):
        master_path = os.path.join(DOCS_DIR, "master-evidence.md")
        with open(master_backup, "r", encoding="utf-8") as src:
            with open(master_path, "w", encoding="utf-8") as dst:
                dst.write(src.read())
        restored += 1

    print(f"Restored {restored} file(s) from backups.")


def main():
    parser = argparse.ArgumentParser(
        description="Merge v1/v2 study content for version toggle",
    )
    parser.add_argument(
        "--restore", action="store_true",
        help="Restore original files from backups",
    )
    args = parser.parse_args()

    if args.restore:
        cmd_restore(args)
    else:
        cmd_merge(args)


if __name__ == "__main__":
    main()
