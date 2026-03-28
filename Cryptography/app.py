from flask import Flask, request, jsonify
import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
import base64
import time

app = Flask(__name__)

MASTER_SECRET = "SuperSecretKey"

# Generate ONE persistent RSA keypair (production style)
rsa_key = RSA.generate(2048)
private_key = rsa_key
public_key = rsa_key.publickey()

# 30 min rotating secret
def get_rotation_secret():
    interval = int(time.time()) // 1800
    return hashlib.sha256((MASTER_SECRET + str(interval)).encode()).hexdigest()

# Flag generator
def generate_flag(team_name, payload):
    rotation_secret = get_rotation_secret()
    raw = payload + team_name + rotation_secret
    return "FLAG{" + hashlib.sha256(raw.encode()).hexdigest()[:32] + "}"

@app.route("/challenge", methods=["POST"])
def challenge():
    team_name = request.json["team_name"]

    payload = "ACCESS_GRANTED"

    rotation_secret = get_rotation_secret()

    # AES key derived from team + rotation
    aes_key = hashlib.sha256((team_name + rotation_secret).encode()).digest()[:16]

    # AES encryption
    aes_cipher = AES.new(aes_key, AES.MODE_ECB)
    ciphertext = aes_cipher.encrypt(pad(payload.encode(), 16))

    # RSA encrypt the AES key (hybrid crypto model)
    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_key = rsa_cipher.encrypt(aes_key)

    return jsonify({
        "encrypted_key": base64.b64encode(encrypted_key).decode(),
        "ciphertext": base64.b64encode(ciphertext).decode(),
        "rsa_public_key": public_key.export_key().decode(),
        "hint": "Decrypt RSA to get AES key. AES key = SHA256(team_name + rotation_secret)[:16]"
    })

@app.route("/validate", methods=["POST"])
def validate():
    team_name = request.json["team_name"]
    submitted_flag = request.json["flag"]

    correct_flag = generate_flag(team_name, "ACCESS_GRANTED")

    if submitted_flag == correct_flag:
        return jsonify({"status": "correct"})
    return jsonify({"status": "wrong"})

if __name__ == "__main__":
    app.run(port=5001)
