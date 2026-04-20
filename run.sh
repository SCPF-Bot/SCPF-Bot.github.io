#!/bin/bash
set -e  # stop on error

# Ensure we are in the repository root
cd "$GITHUB_WORKSPACE" || exit 1

echo "Running restructure in: $(pwd)"

# Create target directory
mkdir -p pages/_collections/diary/_posts

# Find all diary.index.YEAR/_posts folders and move contents
for src in pages/_collections/diary.index.20*/_posts; do
  if [ -d "$src" ]; then
    echo "Moving files from $src"
    # Use a loop to avoid "argument list too long"
    for file in "$src"/*; do
      if [ -f "$file" ]; then
        mv "$file" pages/_collections/diary/_posts/
      fi
    done
    # Remove empty source _posts folder and its parent year folder
    rmdir "$src" 2>/dev/null || true
    rmdir "$(dirname "$src")" 2>/dev/null || true
  fi
done

echo "Restructure complete"

