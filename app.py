from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import edge_tts
from io import BytesIO
import asyncio
from responses import get_response

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def handle_command():
    try:
        data = request.get_json()
        user_input = data.get('text', '').strip()
        
        if not user_input:
            return jsonify({'error': 'Empty input'}), 400
            
        response = get_response(user_input)
        return jsonify({
            'response': response or 'மன்னிக்கவும், இந்த தகவல் கிடைக்கவில்லை.'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/text-to-speech', methods=['POST'])
async def handle_tts():
    try:
        data = request.get_json()
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Empty text'}), 400

        # Create async task for TTS generation
        mp3_buffer = BytesIO()
        communicate = edge_tts.Communicate(text, "ta-IN-PallaviNeural")
        
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                mp3_buffer.write(chunk["data"])
                
        mp3_buffer.seek(0)
        return send_file(
            mp3_buffer,
            mimetype='audio/mpeg',
            download_name='response.mp3'
        )
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)