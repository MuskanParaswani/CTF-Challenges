https://surrey-hudson-present-bookmarks.trycloudflare.com
⸻

Dynamic Steganography CTF Challenge Implementation

1. Challenge Overview

The challenge created is a dynamic steganography challenge hosted on a Capture The Flag (CTF) platform. In this challenge, the participant must extract a hidden flag from an image file using steganography techniques.

The challenge uses the steghide tool to hide the flag inside an image. The flag is protected with a password. To increase the difficulty level, the challenge was designed as a dynamic challenge, meaning that every time the challenge page refreshes, both the flag and the steghide password change automatically.

This prevents participants from sharing flags with others and forces each participant to solve the challenge independently.

⸻

2. Challenge Goal

The goal of the challenge is for participants to:
	1.	Download the provided image file.
	2.	Identify that the file contains hidden data.
	3.	Use steganography tools to extract the hidden data.
	4.	Enter the correct password.
	5.	Retrieve the hidden flag.
	6.	Submit the flag on the CTF platform.

⸻

3. Tools and Technologies Used

Docker

Docker was used to run the CTF platform inside a containerized environment. This allowed easy deployment and management of the CTF infrastructure.

Docker ensured that all dependencies and services required for the challenge ran consistently.

⸻

CTFd

CTFd was used as the main platform to host the challenge. It provides an admin dashboard where challenges can be created, managed, and monitored.

Using CTFd, the challenge description, flag validation, and user interaction were managed.

⸻

Ngrok

Ngrok was used to expose the locally running CTF server to the internet. Since the CTFd platform was running locally using Docker, Ngrok generated a public URL that allowed participants to access the challenge remotely.

⸻

Steghide

Steghide is a steganography tool used to hide data inside images or audio files.

In this challenge, steghide was used to:
	•	Embed the flag inside an image file
	•	Protect the hidden data with a password
	•	Allow extraction only with the correct password

Example command used:

steghide embed -cf image.jpg -ef flag.txt -p password

To extract the hidden data:

steghide extract -sf image.jpg


⸻

4. Challenge Architecture

The challenge system consists of the following components:
	1.	CTFd Platform – Hosts the challenge and validates submitted flags.
	2.	Docker Container – Runs the CTFd application.
	3.	Dynamic Script – Generates a new flag and password whenever the page refreshes.
	4.	Steganography Image File – Contains the hidden flag using steghide.
	5.	Ngrok Tunnel – Makes the local CTF server accessible to participants.

⸻

5. Dynamic Flag and Password Mechanism

Unlike static CTF challenges, this challenge generates new values dynamically.

Every time the challenge page refreshes:
	•	A new random password is generated.
	•	A new flag is generated.
	•	The flag is embedded into the image using steghide.
	•	The updated image file is provided to the participant.

Example format:

Flag: FLAG{random_string}

Password: randomly_generated_password

This ensures that each participant receives a unique challenge instance.

⸻

6. Implementation Steps

The challenge was implemented using the following steps:
	1.	Installed Docker and deployed the CTFd platform.
	2.	Created the challenge through the CTFd admin dashboard.
	3.	Prepared an image file to use for the steganography challenge.
	4.	Generated dynamic flags and passwords using a script.
	5.	Embedded the flag into the image using the steghide tool.
	6.	Configured the system so that the flag and password regenerate when the page refreshes.
	7.	Used Ngrok to expose the local CTF server to the internet.
	8.	Tested the challenge to confirm that the dynamic behavior works correctly.

⸻

7. Challenge Solving Process

To solve the challenge, a participant must:
	1.	Download the provided image file from the challenge page.
	2.	Analyze the file to determine that it contains hidden data.
	3.	Use a steganography tool such as steghide.
	4.	Enter the correct password.
	5.	Extract the hidden flag.
	6.	Submit the flag on the CTFd platform.

⸻

8. Result

The challenge was successfully deployed on the CTFd platform using Docker and Ngrok. The dynamic system correctly generates new flags and passwords for every refresh, ensuring that the challenge remains unique for each attempt.

This design improves challenge security and increases the difficulty level for participants.

⸻
