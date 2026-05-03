from flask import Flask, render_template, request
import os
import random
from werkzeug.utils import secure_filename
from utils.feature_extractor import extract_features
from utils.caption_generator import generate_caption
from gtts import gTTS

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
AUDIO_FOLDER = 'static/audio'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(AUDIO_FOLDER, exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
def index():
    caption = ""
    audio_file = ""
    image_url = ""

    if request.method == 'POST':

        if 'image' not in request.files:
            return "No file uploaded"

        file = request.files['image']

        if file.filename == '':
            return "No selected file"

        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # ✅ IMAGE URL (THIS FIX MAKES IMAGE STAY)
        image_url = "/" + filepath.replace("\\", "/")

        # =========================
        # CAPTION GENERATION
        # =========================
        try:
            features = extract_features(filepath)
            caption = generate_caption(features)

        except Exception as e:
            print("Model Error:", e)
            caption = "A detected object is shown in the image"

        # =========================
        # AUDIO GENERATION
        # =========================
        try:
            tts = gTTS(text=caption, lang='en')
            audio_path = os.path.join(AUDIO_FOLDER, "output.mp3")
            tts.save(audio_path)

            audio_file = "/" + audio_path.replace("\\", "/") + "?v=" + str(random.randint(1, 9999))

        except Exception as e:
            print("TTS Error:", e)
            audio_file = ""

    return render_template(
        'index.html',
        caption=caption,
        audio=audio_file,
        image_url=image_url
    )


if __name__ == '__main__':
    app.run(debug=True)