# Text Cleaner

A small command-line tool, written in Python, that tidies up messy text files.

## What it does
- Collapses repeated spaces and tabs
- Trims spaces from the start and end of each line
- Reduces multiple blank lines to one
- Optionally converts text to lowercase (`--lowercase`)
- Optionally removes duplicate lines (`--remove-duplicates`)

## Requirements
Python 3.8 or newer. No extra packages needed.

## Usage
```
python text_cleaner.py sample_input.txt
python text_cleaner.py sample_input.txt -o result.txt --lowercase --remove-duplicates
```
By default the result is saved next to the input as `<name>_cleaned.txt`.

## What I learned
Working with files using `pathlib`, regular expressions with `re`, and building a command-line interface with `argparse`.