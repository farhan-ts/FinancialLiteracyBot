from flask import Flask, render_template, request, send_file
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from gtts import gTTS
import os
from langdetect import detect

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("jai558/financial-qna-gpt2")
model = AutoModelForCausalLM.from_pretrained("jai558/financial-qna-gpt2")

language_codes = {
    "kn": "Kannada",
    "ta": "Tamil",
    "or": "Odia",
    "bn": "Bengali",
    "mr": "Marathi",
    "en": "English"
}

def generate_answer(question, language_code):
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
        question = request.form["question"]
        input_language = detect(question)

        #Check if the input language is one of the supported languages.
        if input_language in language_codes:
            lang_code = input_language
        else:
            lang_code = 'en' #default to english.

        answer = generate_answer(question, lang_code)
        tts = gTTS(text=answer, lang=lang_code)
        audio_file = "answer.mp3"
        tts.save(audio_file)

    return render_template("index.html", answer=answer, audio_file=audio_file)

@app.route('/audio')
def get_audio():
    audio_file = request.args.get('audio_file')
    if audio_file and os.path.exists(audio_file):
        return send_file(audio_file, mimetype='audio/mpeg', as_attachment=True, download_name='answer.mp3')
    else:
        return "Audio file not found", 404

if __name__ == "__main__":
    app.run(debug=True)