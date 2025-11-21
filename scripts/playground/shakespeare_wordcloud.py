# Shakespeare Word Cloud Generator
# scripts/playground/shakespeare_wordcloud.py

from pathlib import Path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

SHAKESPEARE_STOPWORDS = {
    "thou", "thee", "thy", "thine", "ye",
    "shall", "unto", "tis", "the", "and", "but",
    "from", "with", "for", "that", "this", "what",
    "hath", "doth", "art", "here", "there",
    "a", "an", "to", "of", "in", "on", "is", "be"
}

def clean_text(text: str) -> str:
    """Remove punctuation, extra spaces, and lowercase everything"""
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.lower()

raw_folder = Path(__file__).resolve().parents[2] / "data/raw/playground"

plays = {
    "hamlet.txt": "Blues",               # Melancholic blue
    "macbeth.txt": "inferno",            # Tragic red 
    "romeo_and_juliet.txt": "Purples"    # Purple romance
}

for play_file, colormap in plays.items():
    input_path = raw_folder / play_file

    if not input_path.exists():                                     # Check if file exists
        print(f"File not found : {input_path}")
        continue

    text = clean_text(input_path.read_text(encoding="utf-8"))       # Read and clean text

    wc = WordCloud(
        width=800,
        height=400,
        background_color="black",
        stopwords=SHAKESPEARE_STOPWORDS,
        colormap=colormap
    ).generate(text)

    output_name = f"wordcloud_{play_file.replace('.txt','')}.png"   # Define output path
    output_path = Path(__file__).parent / output_name

    wc.to_file(output_path)                                         # Save Word Cloud image
    print(f"✅ Word Cloud saved: {output_path}")

    plt.figure(figsize=(12,6))                                      # Display Word Cloud
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()

