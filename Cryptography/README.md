# Smart CTF Challenge Server

This repository contains the CTF Crypto Challenge server.

## 🚀 Features
- AES + RSA challenge generation
- Flask server (Python 3.10)
- Dockerized for easy deployment
- Ready to integrate with CTFd

## 📝 Files
- `app.py` — main Flask application
- `Dockerfile` — build Docker image
- `requirements.txt` — Python dependencies
- `.gitignore` — ignore unnecessary files

## 🔧 Usage

### Local Python
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 app.py
