from flask import Flask, render_template, request, send_file, jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from gtts import gTTS
import os
from langdetect import detect
from googletrans import Translator

app = Flask(__name__)

# Load AI model
tokenizer = AutoTokenizer.from_pretrained("jai558/financial-qna-gpt2")
model = AutoModelForCausalLM.from_pretrained("jai558/financial-qna-gpt2")

# Supported languages
language_codes = {
    "kn": "Kannada",
    "ta": "Tamil",
    "or": "Odia",
    "bn": "Bengali",
    "mr": "Marathi",
    "hi": "Hindi",
    "en": "English"
}

def generate_answer(question, language_code):
    """Generates answer using the AI model"""
    inputs = tokenizer(question, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=150)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    audio_file = None
    
    if request.method == "POST":
        question = request.form.get("question", "").strip()

        if not question:
            return render_template("index.html", answer="Please enter or speak a question.", audio_file=None)

        try:
            input_language = detect(question)
            translator = Translator()

            # If the detected language is Hindi, translate to English
            if input_language == "hi":
                question = translator.translate(question, src='hi', dest='en').text
                input_language = "en"

            # Check if the detected language is supported
            lang_code = input_language if input_language in language_codes else "en"

            # Generate response
            answer = generate_answer(question, lang_code)

            # Convert text to speech
            tts = gTTS(text=answer, lang=lang_code)
            audio_file = "answer.mp3"
            tts.save(audio_file)
        
        except Exception as e:
            answer = f"Error processing request: {str(e)}"
            audio_file = None

    return render_template("index.html", answer=answer, audio_file=audio_file)

@app.route('/audio')
def get_audio():
    """Serves the generated audio response"""
    audio_file = request.args.get('audio_file')
    if audio_file and os.path.exists(audio_file):
        return send_file(audio_file, mimetype='audio/mpeg', as_attachment=True, download_name='answer.mp3')
    return "Audio file not found", 404

if __name__ == "__main__":
    app.run(debug=True)
