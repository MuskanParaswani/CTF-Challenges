# SmartOSINT

## Category

OSINT / Web

## Difficulty

Easy-Medium

## Description

A mysterious digital identity has left traces online.
Investigate and uncover hidden information.

## Setup (Docker)

```bash
docker build -t smartosint .
docker run -p 5002:5002 smartosint
```

## Setup (Manual)

```bash
pip install -r requirements.txt
python3 app.py
```

Open:
http://127.0.0.1:5002

## Notes

* Dynamic flag based on user input
* Check source code carefully

## Flag Format

flag{...}
