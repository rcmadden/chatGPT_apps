from flask import Flask, render_template, request, jsonify, send_from_directory
from gtts import gTTS
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

voice_options = {
    'en': {
        'name': 'English',
        'options': {
            'en-us': 'English (US)',
            'en-uk': 'English (UK)'
        }
    },
    'es': {
        'name': 'Spanish',
        'options': {
            'es-us': 'Spanish (US)',
            'es-es': 'Spanish (Spain)'
        }
    }
    # Add more languages and voice options as needed
}

@app.route('/')
def index():
    return render_template('index.html', voice_options=voice_options)

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    voice_type = request.form['voice_type']
    tts = gTTS(text=text, lang=voice_type, slow=False)
    tts.save(os.path.join(app.config['UPLOAD_FOLDER'], 'output.mp3'))
    audio_src = request.host_url + 'static/output.mp3'
    return jsonify({'audio_src': audio_src})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
