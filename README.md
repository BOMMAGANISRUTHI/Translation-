# 🌐 Language Translation Tool — CodeAlpha Task 1

A clean, fast web app that translates text between 25+ languages in real time.

## Features
- Type and translate instantly (auto-translates as you type, debounced)
- Auto-detect source language
- Swap source ⇄ target languages with one tap
- Copy translated text
- Listen to the translation (text-to-speech via browser)
- Responsive: side-by-side on desktop, stacked on mobile

## Tech Stack
- **Python + Flask** — backend & API route
- **deep-translator** — free translation engine (Google Translate backend, no API key needed)
- **HTML/CSS/JS** — frontend, no frameworks

## Project Structure
```
language-translator/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── README.md
```

## Run Locally
```bash
git clone https://github.com/BOMMAGANISRUTHI/language-translator.git
cd language-translator
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`

## Deploy (Render, free)
1. Push this repo to GitHub
2. Render → New + → Web Service → connect repo
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `gunicorn app:app`
5. Instance Type: Free

## Author
**Sruthi Bommagani** — CodeAlpha Internship, Task 1: Language Translation Tool
