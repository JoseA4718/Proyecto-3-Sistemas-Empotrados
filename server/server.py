from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde cualquier origen

# Global variable to store the state
global global_state 
global_state = "stop"

@app.route('/send_command', methods=['POST'])
def send_command():
    global global_state
    data = request.json
    command = data.get('command', '')
    print(f"Comando recibido: {command}")
    
    global_state = command

    print(f"Nuevo estado: {global_state}")
    
    return jsonify({"status": "success", "received": command, "state": global_state})

@app.route('/get_state', methods=['GET'])
def get_state():
    global global_state
    return jsonify({"state": global_state})

@app.route('/reset_state', methods=['GET'])
def reset_state():
    global global_state 
    global_state = "play"
    print(f"Estado reiniciado a: {global_state}")
    return jsonify({"status": "success", "state": global_state})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
