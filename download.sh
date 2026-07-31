#!/usr/bin/env bash

# This script grabs the puzzles directly from the project euler website.
# Creates the first version in Python and adds a new entry to the
# completed.json file
# REQUIRES: wget, jq

set -euo pipefail

puzzlenum="${1:-}"

if [ -z "${puzzlenum}" ]; then
    echo "Project Euler puzzle downloader"
    echo "Creates the directory and sets up the puzzle in Python."
    echo "Usage: $0 <puzzle_number>"
    exit 1
fi

# check if wget is installed before continuing
if ! command -v wget &>/dev/null; then
    echo "wget is not installed. Cannot download puzzles."
    echo "Download wget to use this script"
    exit 1
fi

# also check for jq
if ! command -v jq &>/dev/null; then
    echo "jq is not installed. Cannot add new entry to completed.json"
    echo "Install jq to use this script"
    exit 1
fi

# check if the puzzlenum is a valid number
if ! [[ "$puzzlenum" =~ ^[0-9]+$ ]]; then
    echo "Invalid puzzle number: $puzzlenum"
    exit 1
fi

echo "Puzzle: ${puzzlenum}"

# Get the directory of this script
SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# first we gotta extract the puzzle name
puzzlename=$(wget -qO- "https://projecteuler.net/problem=$puzzlenum" | grep -oP '(?<=<h2>).*?(?=</h2>)')

echo "Puzzle name: $puzzlename"

# replace all spaces with underscores:
puzzlename_clean=$(echo "$puzzlename" | tr '[:upper:] ' '[:lower:]_')
name_with_number="$puzzlenum"_"$puzzlename_clean"

puzzledir="$SCRIPTDIR/solutions/$name_with_number"

# check if the directory already exists
if [ -d "$puzzledir" ]; then
    echo "Error: Directory already exists:"
    echo "$puzzledir"
    exit 1
fi

# create a directory for the puzzle
mkdir -p "$puzzledir"

filepath="$puzzledir/$puzzlenum.py"

# print opening triple quotes to the file, and download it
echo '"""' > "$filepath"
wget -qO- "https://projecteuler.net/minimal=$puzzlenum" >> "$filepath" && \

# closing triple quotes
echo '"""' >> "$filepath"

echo "Created $name_with_number/$puzzlenum.py"

# Extract and download any images (if any exist)
if grep -q '<img src=' "$filepath"; then \
    grep -oP '(?<=<img src=")[^"]+?\.(png|gif|jpg|jpeg)' "$filepath" | \
    while read img_url; do \
        wget -q -P "$puzzledir" "https://projecteuler.net/$img_url"; \
    done; \
fi

# cleanup the file
sed -i \
-e 's|\$||g' \
-e 's|\\to|->|g' \
-e 's|\\cdots|...|g' \
-e 's|\\dots|...|g' \
-e 's|\\times|*|g' \
-e 's|\\mathbf||g' \
-e 's|{align}||g' \
-e 's|\\begin||g' \
-e 's|\\end||g' \
-e 's|&amp;\\colon|:|g' \
-e 's|<img[^>]*>|* see image *|g' \
-e 's|<br>|\n|g' \
-e 's|<[^>]*>||g' \
"$filepath"

# remove all blank lines then word wrap
sed -i '/^[[:space:]]*$/d' "$filepath"
fold -s "$filepath" > "$filepath.tmp" && mv "$filepath.tmp" "$filepath"


# add new entry to completed.json
jsonpath="$SCRIPTDIR/completed.json"
tmppath="$jsonpath.tmp"

# --arg u "$puzzlenum" passes puzzlenum into the $u variable.
# .[$u] // {} ensures that if .[$u] doesn't exist yet, it defaults to an
#     empty object {} instead of failing.
# + { ... } merges the new key-value pairs directly into that object without 
#     overwriting other existing keys that might be inside .[$u].
jq --arg u "$puzzlenum" '
  .[$u] = (.[$u] // {}) + {
    "python": "❌",
    "typescript": "❌",
    "go": "❌"
  }
' "$jsonpath" > "$tmppath" && mv "$tmppath" "$jsonpath"
