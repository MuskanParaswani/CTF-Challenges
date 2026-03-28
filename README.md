# CTF-Challenges
Dynamic CTF Challenge Platform Implementation

 

1. Introduction

This project focuses on the development and deployment of multiple dynamic Capture The Flag (CTF) challenges using the CTFd platform. The challenges were designed to simulate real-world cybersecurity scenarios and encourage participants to apply skills in cryptography, web security, steganography, OSINT, and network forensics. To ensure scalability and isolation, the platform was deployed using Docker containers. Ngrok was used to expose the locally hosted challenge server to the internet, allowing remote access for participants.

2. Dynamic Steganography Challenge

2.1 Overview
This challenge requires participants to extract a hidden flag from an image file using steganography techniques. The flag is embedded using the steghide tool and protected with a password.

2.2 Dynamic Mechanism

To prevent flag sharing between participants, the system dynamically generates a new flag and password every time the challenge page refreshes. The new flag is embedded into the image automatically before being delivered to the participant.

2.3 Tools Used

Docker – Containerized deployment of the CTF platform.

CTFd – Challenge hosting and flag validation.

Ngrok – Exposes the local CTF server to the internet.

Steghide – Tool used to embed hidden data inside image files.

2.4 Example Commands

Embedding a flag into an image:

steghide embed -cf image.jpg -ef flag.txt -p password

Extracting hidden data:

steghide extract -sf image.jpg

2.5 Result

The dynamic steganography challenge was successfully implemented. Each refresh generates a new flag and password, ensuring that participants must independently solve the challenge.

3. Hybrid Cryptography Challenge (RSA + AES)

3.1 Overview

This challenge demonstrates hybrid cryptography using RSA and AES encryption. The goal is to retrieve a hidden flag by decrypting challenge data provided by the server.

3.2 Technologies Used

Python – Backend challenge logic.

Flask – API server framework.

Docker – Containerized deployment.

Gunicorn – Production server.

RSA – Asymmetric encryption.

AES – Symmetric encryption.

SHA256 – Key derivation.

Ngrok – Public access to the server.

GitHub – Source code management.

3.3 Challenge Workflow

Participants send their team name to the challenge API endpoint. The server generates a team-specific AES key using SHA256 hashing. The flag is encrypted using AES-CBC encryption. The AES key is then encrypted using RSA before being returned to the participant.

3.4 Flag Format

CTF{...}

3.5 Deployment

Docker Build: docker build -t serious-crypto .

Docker Run: docker run -p 5001:5001 serious-crypto

4. Dynamic OSINT Challenge

4.1 Overview

This challenge requires participants to investigate a webpage and discover hidden information that leads to the correct flag.

4.2 Dynamic Features

Time-Based Flag Rotation – Flags change periodically.

User-Specific Flags – Each team receives a unique flag.

Hidden Web Flags – Flags are embedded in webpage source code.

Adaptive Scoring – Points decrease as more teams solve the challenge.

4.3 Result

The OSINT challenge successfully generates dynamic flags for each user and ensures fairness by preventing flag reuse.

5. Web Security Challenge (Burp Suite)

5.1 Objective

The objective of this challenge is to analyze and manipulate web application requests using Burp Suite to discover hidden information and retrieve the flag.

5.2 Solving Steps

Access the challenge URL and enter the required information.

Configure the browser to route traffic through Burp Suite Proxy.

Intercept HTTP requests sent to the server.

Analyze request parameters for potential manipulation.

Modify the request before forwarding it to the server.

Observe the server response.

Retrieve the flag hidden in the response.

6. Network Forensics Challenge

6.1 Objective

This challenge requires participants to analyze captured network traffic and identify hidden data transmitted during a communication session.

6.2 Scenario

Participants receive a PCAP file containing recorded network traffic. Within this traffic, an image file was transferred which contains a hidden flag.

6.3 Investigation Steps

Open the PCAP file in Wireshark.

Use the Follow TCP Stream feature to reconstruct communication.

Identify the transferred image file.

Extract the image from the network capture.

Convert the image into raw format if required.

Analyze the image for hidden data.

Decode the hidden flag.

7.Challange Description 
A web application implements a broken session mechanism.

• A new session token is generated on every reload  
• The session token is exposed to the client 
• The flag is user-specific and time-based  
• Flags rotate every 60 seconds  

Challenge URL:http://127.0.0.1:8000

Goal:Analyze the application behavior and submit the correct flag before it expires.

9. Conclusion

This project demonstrates how multiple cybersecurity challenges can be implemented within a dynamic CTF environment. By combining technologies such as Docker, CTFd, Flask, and modern cryptographic techniques, the system provides realistic and interactive challenges for participants. The dynamic flag generation ensures fairness and prevents solution sharing between teams.
