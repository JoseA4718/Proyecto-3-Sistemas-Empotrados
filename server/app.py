from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir solicitudes desde cualquier origen

@app.route('/send_command', methods=['POST'])
def send_command():
    data = request.json
    command = data.get('command', '')
    print(f"Comando recibido: {command}")
    return jsonify({"status": "success", "received": command})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)