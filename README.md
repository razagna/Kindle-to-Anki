# Kindle-to-Anki
A web-scraping application that takes a word list export from **K**indle highlights and converts them into Japanese-English flashcards compatible with **A**nki.

![screenshot](./kindle-to-anki.jpg)

## Usage
1. Install the requirements
```bash
python3 -m pip install -r requirements.txt 
```
2. Run the GUI application
```bash
python3 src/kindle-to-anki.py
```

## Output
The resulting flash-cards have the following contents and format.

### Contents

The information that gets fetched from [Jisho](https://jisho.org) includes:
- the Japanese word
- its English translation
- a randomly selected example sentence
- the reading of the example sentence with furigana
- the English translations of the example sentence

### Format

Supported output formats are: 
- Excel spreedsheets (.xlsx)
- Anki packages (.apkg)