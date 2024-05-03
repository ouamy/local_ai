import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enables CORS for all routes

@app.route('/sendMessage', methods=['POST'])
def send_message():
    data = request.get_json()
    input_text = data['inputText']

    # execute command and capture output
    command_output = subprocess.run(['ollama', 'run', 'llama3', input_text], capture_output=True, text=True)

    # check if command was successful
    if command_output.returncode == 0:
        output = command_output.stdout.strip()
    else:
        output = "Error: Command execution failed"

    return jsonify({'output': output})

if __name__ == "__main__":
    app.run(port=8000)  # run Flask app on port 8000
