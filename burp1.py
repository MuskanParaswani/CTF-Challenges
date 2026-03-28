from flask import Flask, request

app = Flask(__name__)

FLAG = "CTF{burp_role_escalation_success}"

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure Login</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }

            .card {
                background: rgba(255, 255, 255, 0.08);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                text-align: center;
                width: 350px;
            }

            h2 {
                margin-bottom: 25px;
                letter-spacing: 1px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border-radius: 8px;
                border: none;
                outline: none;
                font-size: 14px;
            }

            button {
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: none;
                background: #00c6ff;
                background: linear-gradient(to right, #0072ff, #00c6ff);
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                transform: scale(1.05);
                box-shadow: 0 0 15px #00c6ff;
            }

            .footer {
                margin-top: 20px;
                font-size: 12px;
                opacity: 0.7;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>🔐 Cipher Access Portal</h2>
            <form method="POST" action="/login">
                <input type="text" name="username" placeholder="Enter Username" required>
                <button type="submit">Login</button>
            </form>
            <div class="footer">
                Authorized Personnel Only
            </div>
        </div>
    </body>
    </html>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    role = "user"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard Access</title>
        <style>
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #141e30, #243b55);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                color: white;
            }}

            .card {{
                background: rgba(255, 255, 255, 0.08);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
                text-align: center;
                width: 350px;
            }}

            button {{
                width: 100%;
                padding: 12px;
                border-radius: 8px;
                border: none;
                background: linear-gradient(to right, #ff512f, #dd2476);
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }}

            button:hover {{
                transform: scale(1.05);
                box-shadow: 0 0 15px #ff512f;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Welcome {username}</h2>
            <p>Your Role: {role}</p>
            <form method="POST" action="/dashboard">
                <input type="hidden" name="username" value="{username}">
                <input type="hidden" name="role" value="{role}">
                <button type="submit">Enter Dashboard</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.route("/dashboard", methods=["POST"])
def dashboard():
    role = request.form.get("role")

    if role == "admin":
        return f"""
        <body style="background:black;color:lime;font-family:monospace;text-align:center;padding-top:100px;">
            <h1>⚡ ADMIN ACCESS GRANTED ⚡</h1>
            <h2>{FLAG}</h2>
        </body>
        """
    else:
        return """
        <body style="background:#1f1f1f;color:red;font-family:monospace;text-align:center;padding-top:100px;">
            <h1>❌ ACCESS DENIED</h1>
            <p>Insufficient Privileges</p>
        </body>
        """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)