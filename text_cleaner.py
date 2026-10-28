"""Text Cleaner: tidy up messy text files from the command line.

Usage:
    python text_cleaner.py sample_input.txt
    python text_cleaner.py sample_input.txt -o result.txt --lowercase --remove-duplicates
"""

import argparse
import re
import sys
from pathlib import Path


def clean_text(text, lowercase=False, remove_duplicates=False):
    """Return a cleaned version of `text`.

    - Collapses repeated spaces/tabs into a single space
    - Strips spaces from the start and end of every line
    - Shrinks runs of blank lines down to a single blank line
    - Optionally lowercases everything
    - Optionally removes duplicate lines (case-insensitive)
    """
    cleaned_lines = []
    seen = set()

    for line in text.splitlines():
        line = re.sub(r"[ \t]+", " ", line).strip()

        if lowercase:
            line = line.lower()

        if remove_duplicates and line:
            key = line.lower()
            if key in seen:
                continue
            seen.add(key)

        cleaned_lines.append(line)

    result = "\n".join(cleaned_lines)
    result = re.sub(r"\n{3,}", "\n\n", result)  # max one blank line in a row
    return result.strip() + "\n"


def main():
    parser = argparse.ArgumentParser(description="Clean up messy text files.")
    parser.add_argument("input", help="path to the text file to clean")
    parser.add_argument("-o", "--output", help="where to save the result "
                        "(default: <input>_cleaned.txt)")
    parser.add_argument("--lowercase", action="store_true",
                        help="convert all text to lowercase")
    parser.add_argument("--remove-duplicates", action="store_true",
                        help="remove duplicate lines")
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.is_file():
        sys.exit(f"Error: file not found: {input_path}")

    output_path = (Path(args.output) if args.output
                   else input_path.with_name(f"{input_path.stem}_cleaned.txt"))

    original = input_path.read_text(encoding="utf-8")
    cleaned = clean_text(original, args.lowercase, args.remove_duplicates)
    output_path.write_text(cleaned, encoding="utf-8")

    print(f"Cleaned {len(original.splitlines())} lines -> "
          f"{len(cleaned.splitlines())} lines")
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    main() 
