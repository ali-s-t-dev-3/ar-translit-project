# Arabic Transliteration Tool

Live demo: https://ali-s-t-dev-3.github.io/ar-translit-project/

A transliteration tool that turns Latin/Arabizi-style input into Arabic script. The original project is a Python prototype with dictionary lookup and next-word prediction; the public website ports the same core logic into browser JavaScript so it can run on GitHub Pages.

## Features

- Longest-match transliteration rules for Latin input.
- Arabic dictionary suggestions ranked by word frequency.
- Bigram-based next-word prediction.
- Tkinter Python prototype preserved in `frontend.py`.
- Static browser demo in `docs/` for CV and portfolio sharing.

## Run the Python Prototype

```powershell
python frontend.py
```

The Tkinter version depends on `arabic_reshaper`.

## Run the Website Locally

Open `docs/index.html` in a browser, or serve the repo locally:

```powershell
python -m http.server 8000
```

Then visit `http://localhost:8000/docs/`.

## Test

```powershell
npm test
```

## Tech Stack

- Python prototype: `backend.py`, `frontend.py`
- Browser demo: HTML, CSS, JavaScript modules
- Hosting: GitHub Pages from the `docs/` folder
