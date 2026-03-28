import random
import string
import subprocess
from flask import Flask, render_template, send_from_directory
import os
import time

app = Flask(__name__)

STATIC_DIR = "static"

def generate_flag():
    """Random 12-character flag"""
    return "FLAG{" + ''.join(random.choices(string.ascii_letters + string.digits, k=12)) + "}"

def generate_password():
    """Random 8-character password"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

@app.route("/")
def challenge():
    flag = generate_flag()
    password = generate_password()
    timestamp = str(int(time.time()))
    
    temp_flag_file = f"flag_{timestamp}.txt"
    temp_image_file = f"{STATIC_DIR}/challenge_{timestamp}.jpg"

    # Save the flag temporarily
    with open(temp_flag_file, "w") as f:
        f.write(flag)

    # Copy base image to temporary stego image
    base_image = f"{STATIC_DIR}/image.jpg"
    subprocess.run(["cp", base_image, temp_image_file])

    # Embed flag in the temp image
    subprocess.run([
        "steghide", "embed",
        "-cf", temp_image_file,
        "-ef", temp_flag_file,
        "-p", password,
        "-q"
    ])

    # Remove temporary flag file
    os.remove(temp_flag_file)

    # Render HTML page showing password in page source
    return render_template("index.html",
                           password=password,
                           filename=f"challenge_{timestamp}.jpg")

# Serve dynamic images
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(STATIC_DIR, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
