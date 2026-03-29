
1. Project Title
AI-Based Dynamic Hybrid Cryptography Challenge System for CTF Platform

2. Objective of the Project
The objective of this project is to design and implement a dynamic cryptography challenge system for a Capture The Flag (CTF) competition.
The system generates unique encrypted challenges for each team and automatically updates encryption parameters every 30 minutes, ensuring fairness, security, and difficulty in solving the challenge.
This project demonstrates practical implementation of:
Cryptography
Secure API design
Dynamic key rotation
Containerized deployment

3. Problem Statement
Traditional CTF challenges use static encryption methods where:
All teams receive the same challenge
Solutions can be shared between teams
Security risks increase
This project solves the problem by:
Generating team-specific encrypted challenges
Rotating secrets every 30 minutes
Preventing solution reuse

4. Project Overview
This project implements a dynamic hybrid encryption challenge server that uses:
AES encryption for message protection
RSA encryption for key protection
SHA256 hashing for generating team-based keys
Time-based rotation mechanism
Docker-based deployment
Ngrok-based public access
Participants send their team name to the API, and the server returns encrypted challenge data.

5. System Architecture
Components Used
CTFd Platform
Flask API Server
Hybrid Crypto Engine
Docker Container
Ngrok Tunnel
GitHub Repository

Architecture Flow
User (Team)
      │
      ▼
CTFd Platform
      │
      ▼
Challenge API Server
      │
      ▼
Key Generator (SHA256)
      │
      ▼
AES Encryption
      │
      ▼
RSA Encryption
      │
      ▼
Encrypted Response Sent

6. Technologies Used


7. Encryption Method Used
This project uses Hybrid Encryption, which combines symmetric and asymmetric cryptography.

7.1 AES Encryption
AES (Advanced Encryption Standard) is used to encrypt the main message or flag.
Configuration:
Algorithm: AES
Mode: CBC (Cipher Block Chaining)
Key Size: 128-bit
Output: Ciphertext
Purpose:
Encrypt the actual challenge message
Ensure data confidentiality

7.2 RSA Encryption
RSA encryption is used to protect the AES key.
Configuration:
Algorithm: RSA
Key Size: 2048-bit
Purpose:
Secure transmission of AES key
Prevent direct access to encryption key

7.3 SHA256 Hashing
SHA256 hashing is used to generate dynamic AES keys.
Key Generation Logic:
AES_key = SHA256(team_name + rotation_secret)[:16]
Purpose:
Generate team-specific keys
Ensure uniqueness

8. Dynamic Rotation Mechanism
One of the key features of this project is time-based rotation.
Every 30 minutes:
Rotation secret changes
New AES key generated
New ciphertext created
Benefits:
Prevents reuse of old solutions
Enhances challenge difficulty
Improves fairness

9. API Design
The challenge server exposes an HTTP endpoint.

Endpoint
POST /challenge

Request Format
{
  "team_name": "AlphaTeam"
}

Response Format
{
  "ciphertext": "...",
  "encrypted_key": "...",
  "iv": "...",
  "rsa_public_key": "-----BEGIN PUBLIC KEY-----",
  "hint": "Decrypt RSA to get AES key"
}

10. Docker Deployment
The project uses Docker to ensure portability.

Build Command
docker build -t serious-crypto .

Run Command
docker run -p 5001:5001 serious-crypto

11. Public Exposure Using Ngrok
Ngrok is used to expose the local server to the internet.
Command used:
ngrok http 5001
Example Public URL:
https://evangeline-duddy-gage.ngrok-free.dev

12. Integration with CTF Platform
The system integrates with a CTF platform such as CTFd.
Tasks performed:
Created crypto challenge
Added hints
Configured scoring system
Tested API communication

13. Testing Methodology
Testing was performed using:
Curl Testing
curl -X POST http://localhost:5001/challenge \
-H "Content-Type: application/json" \
-d '{"team_name":"TestTeam"}'
Verified:
JSON response
Encryption accuracy
Dynamic key generation

14. GitHub Repository
Project repository:
https://github.com/anshki24/smart-ctf-challenge-server
Repository contains:
Source code
Docker configuration
Documentation
Setup instructions

15. Security Features
Implemented security mechanisms:
Hybrid encryption
Time-based rotation
Team-specific keys
RSA protected AES key
Unique challenge generation

16. Advantages of the System
Prevents cheating
Ensures fairness
Improves challenge difficulty
Supports scalability
Provides real-world cryptography practice

17. Limitations
Requires internet access
Requires server uptime
Time synchronization required

18. Future Enhancements
Possible improvements:
Add AI-generated dynamic hints
Multi-layer encryption
Database logging
Monitoring dashboard
Automated scaling

19. Conclusion
This project successfully implements a dynamic hybrid cryptography challenge server suitable for CTF competitions.
The system ensures:
Unique team challenges
Secure encryption
Dynamic key rotation
Reliable deployment
It demonstrates real-world application of cryptographic principles and secure system design.

20. Author Contribution (Your Work)
This is very important section.
You can submit this:

My Contribution
In this project, I performed the following tasks:
Designed hybrid encryption logic using AES and RSA
Implemented SHA256-based key generation
Developed Flask API server
Implemented 30-minute rotation mechanism
Created Docker deployment configuration
Configured Ngrok public access
Integrated challenge with CTF platform
Managed GitHub repository
Tested API functionality using curl
Debugged deployment issues
Prepared project documentation

