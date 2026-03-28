from flask import Flask, request, jsonify, send_from_directory
import secrets
from flag_logic import generate_flag

app = Flask(__name__)
sessions = {}

@app.route("/")
def home():
    return send_from_directory("static", "index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory("static", path)

@app.route("/get-token")
def get_token():
    user_id = request.args.get("user", "player1")
    token = secrets.token_hex(8)
    sessions[token] = user_id
    return jsonify({"token": token})

@app.route("/submit-flag", methods=["POST"])
def submit_flag():
    data = request.json
    token = data.get("token")
    flag = data.get("flag")

    if token not in sessions:
        return jsonify({"status": "Invalid token"}), 403

    correct = generate_flag(sessions[token])

    if flag == correct:
        return jsonify({"status": "Correct Flag ✅"})
    else:
        return jsonify({"status": "Wrong Flag ❌"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
