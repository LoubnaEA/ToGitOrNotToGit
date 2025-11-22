# md_to_delim.py
import re, csv
from pathlib import Path

# Lire le fichier markdown
IN = Path("docs/creators.md").read_text(encoding="utf-8").splitlines()

# garder les lignes contenant des pipes et ignorer la ligne de séparation
rows = [r for r in IN if '|' in r and not re.match(r'^\s*\|?[-:\s|]+\|?\s*$', r)]

def split_md_row(row):
    # supprimer les pipes de début et fin
    row = re.sub(r'^\s*\|', '', row)
    row = re.sub(r'\|\s*$', '', row)
    # séparer sur les pipes et enlever les espaces
    cells = [c.strip() for c in re.split(r'\s*\|\s*', row)]
    return cells

# créer la table
table = [split_md_row(r) for r in rows]

# Séparateur désiré
SEP = '|'

# Fichier de sortie
OUT = Path("data/creators_delim.txt")
OUT.parent.mkdir(parents=True, exist_ok=True)

# Écriture CSV
with OUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=SEP, quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in table:
        writer.writerow(row)

print(f"Written {OUT} with separator {SEP!r}. Use pandas.read_csv(..., sep='{SEP}') to load.")
