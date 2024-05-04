import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

session_context = {}

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    input_text = data['inputText']
    session_id = data.get('sessionId')

    context = session_context.get(session_id, [])

    full_input_text = '\n'.join(context + [input_text])

    command_output = subprocess.run(['ollama', 'run', 'llama3', full_input_text], capture_output=True, text=True)

    context.append(input_text)
    session_context[session_id] = context

    if command_output.returncode == 0:
        output = command_output.stdout.strip()
    else:
        output = "Error: Command execution failed"

    return jsonify({'output': output})

if __name__ == "__main__":
    app.run(port=8000)
