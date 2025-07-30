from flask import Flask, render_template, request, Response, stream_with_context
from flask_cors import CORS
import requests
import json
import datetime
import logging

# --- CONFIGURATION ---
OLLAMA_MODEL = "gemma3n:e2b"
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
SYSTEM_PROMPT = """
You are a helpful and knowledgeable health and medical AI assistant.
IMPORTANT: You MUST NOT provide medical advice, diagnoses, or prescriptions.
If the user mentions an emergency (e.g., chest pain, severe bleeding, difficulty breathing), IMMEDIATELY and ONLY advise them to call 911 or their local emergency number.
Keep answers general, informative, and easy to understand.
"""

app = Flask(__name__, template_folder='templates')
CORS(app) # Enable CORS for all routes

# --- LOGGING SETUP ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/')
def index():
    """Serves the main HTML application."""
    return render_template('main.html')

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    """
    Handles user requests, sends them to Ollama, and streams back the response.
    """
    user_input = request.json.get('userInput')
    if not user_input:
        return {"error": "userInput is required"}, 400

    logging.info(f"Received user input: {user_input}")

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": f'{SYSTEM_PROMPT.strip()}\n\nUser question: "{user_input}"',
        "stream": True # Important for streaming response
    }

    def generate():
        try:
            # Send request to Ollama with streaming enabled
            response = requests.post(
                OLLAMA_ENDPOINT,
                json=payload,
                stream=True, # Enable streaming for requests library
                timeout=240 # Increased timeout for potentially long generations
            )
            response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    try:
                        # Ollama sends newline-separated JSON objects
                        lines = chunk.decode('utf-8').split('\n')
                        for line in lines:
                            if line.strip(): # Ensure line is not empty
                                data = json.loads(line)
                                token = data.get("response", "")
                                if token:
                                    # Send each token as a Server-Sent Event (SSE)
                                    yield f"data: {json.dumps({'token': token})}\n\n"
                                if data.get("done"):
                                    # Signal the frontend that the stream is complete
                                    yield "data: {\"done\": true}\n\n"
                                    return # End the generator
                    except json.JSONDecodeError as e:
                        logging.error(f"JSON Decode Error from Ollama chunk: {e} - Chunk: {chunk.decode('utf-8')}")
                        # Continue processing, some chunks might be incomplete JSON
                    except Exception as e:
                        logging.error(f"Error processing Ollama stream chunk: {e}")
                        yield f"data: {json.dumps({'error': 'Error processing AI response'})}\n\n"
                        return

        except requests.exceptions.RequestException as e:
            logging.error(f"Network or API Error with Ollama: {e}")
            yield f"data: {json.dumps({'error': 'Sorry, I\'m having trouble connecting to the AI service. Please ensure Ollama is running.'})}\n\n"
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            yield f"data: {json.dumps({'error': 'An unexpected error occurred on the server.'})}\n\n"

    # Set appropriate headers for Server-Sent Events (SSE)
    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    logging.info("Starting Flask application...")
    # Using host='0.0.0.0' makes it accessible externally if needed,
    # but '127.0.0.1' or 'localhost' is fine for local development.
    # debug=True allows for auto-reloading on code changes.
    app.run(host='127.0.0.1', port=5000, debug=True)