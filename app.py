from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException

app = Flask(__name__)

# Curated list of common languages: code -> display name
LANGUAGES = {
    "auto": "Detect Language",
    "en": "English",
    "hi": "Hindi",
    "te": "Telugu",
    "ta": "Tamil",
    "kn": "Kannada",
    "ml": "Malayalam",
    "mr": "Marathi",
    "bn": "Bengali",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "zh-CN": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "tr": "Turkish",
    "nl": "Dutch",
    "vi": "Vietnamese",
    "th": "Thai",
    "id": "Indonesian",
}

# Target list should not include "auto" (you can't translate TO "detect")
TARGET_LANGUAGES = {k: v for k, v in LANGUAGES.items() if k != "auto"}


@app.route("/")
def index():
    return render_template("index.html", source_langs=LANGUAGES, target_langs=TARGET_LANGUAGES)


@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    source = data.get("source", "auto")
    target = data.get("target", "en")

    if not text:
        return jsonify({"error": "Please enter some text to translate."}), 400

    if len(text) > 4500:
        return jsonify({"error": "Text is too long. Please keep it under 4500 characters."}), 400

    try:
        translated = GoogleTranslator(source=source, target=target).translate(text)
        return jsonify({"translated_text": translated})
    except LanguageNotSupportedException:
        return jsonify({"error": "That language pair isn't supported. Try a different language."}), 400
    except Exception as e:
        return jsonify({"error": f"Translation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
