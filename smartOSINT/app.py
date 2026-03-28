from flask import Flask, request, session, render_template
import hashlib
import secrets
import base64

app = Flask(__name__)
app.secret_key = "SESSION_SECRET_123"

@app.route("/")
def index():
    team = request.args.get("team", "guest")

    persona_id = hashlib.md5(team.encode()).hexdigest()[:6]

    raw_flag = f"flag{{ghost_{persona_id}}}"
    encoded_flag = base64.b64encode(raw_flag.encode()).decode()

    session["encoded_flag"] = encoded_flag

    return render_template("index.html", persona_id=persona_id)

@app.route("/trace")
def trace():
    raw_flag = f"flag{{ghost_{secrets.token_hex(6)}}}"
    encoded_flag = base64.b64encode(raw_flag.encode()).decode()

    return render_template("trace.html", token=encoded_flag)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
