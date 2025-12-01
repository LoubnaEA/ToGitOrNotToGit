import re, csv
from pathlib import Path

# Read the markdown file
IN = Path("docs/creators.md").read_text(encoding="utf-8").splitlines()

# Keep lines containing pipes and ignore the separator line
rows = [r for r in IN if '|' in r and not re.match(r'^\s*\|?[-:\s|]+\|?\s*$', r)]

def split_md_row(row):
    row = re.sub(r'^\s*\|', '', row)         # Remove leading and trailing pipes
    row = re.sub(r'\|\s*$', '', row)
    cells = [c.strip() for c in re.split(r'\s*\|\s*', row)]      # Split on pipes and remove whitespace
    return cells

table = [split_md_row(r) for r in rows]     # Create the table

SEP = '|'

# Output file
OUT = Path("data/creators_delim.txt")
OUT.parent.mkdir(parents=True, exist_ok=True)

# CSV writing
with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=SEP, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in table:
        writer.writerow(row)

print(f"Written {OUT} with separator {SEP!r}. Use pandas.read_csv(..., sep='{SEP}') to load.")