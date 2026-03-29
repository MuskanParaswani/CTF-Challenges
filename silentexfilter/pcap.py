from scapy.all import *
import base64
import random

client = "10.0.0.5"
server = "10.0.0.8"

sport = random.randint(20000,60000)
dport = 80

packets = []

client_seq = 1000
server_seq = 5000

# =========================
# 1️⃣ TCP HANDSHAKE
# =========================

packets.append(IP(src=client,dst=server)/
               TCP(sport=sport,dport=dport,flags="S",seq=client_seq))

packets.append(IP(src=server,dst=client)/
               TCP(sport=dport,dport=sport,flags="SA",seq=server_seq,ack=client_seq+1))

packets.append(IP(src=client,dst=server)/
               TCP(sport=sport,dport=dport,flags="A",seq=client_seq+1,ack=server_seq+1))

client_seq += 1
server_seq += 1

# =========================
# 2️⃣ FAKE HTTP NOISE
# =========================

for i in range(5):
    data = b"GET /index.html HTTP/1.1\r\nHost: example.com\r\n\r\n"
    packets.append(IP(src=client,dst=server)/
                   TCP(sport=sport,dport=dport,flags="PA",
                       seq=client_seq,ack=server_seq)/
                   Raw(load=data))
    client_seq += len(data)

# =========================
# 3️⃣ DNS NOISE
# =========================

for i in range(3):
    packets.append(IP(src=client,dst="8.8.8.8")/
                   UDP(sport=33333+i,dport=53)/
                   Raw(load=b"\xaa\xbb\x01\x00"))

# =========================
# 4️⃣ REAL GET REQUEST
# =========================

real_get = b"GET /assets/logo.png HTTP/1.1\r\nHost: internal.local\r\n\r\n"

packets.append(IP(src=client,dst=server)/
               TCP(sport=sport,dport=dport,flags="PA",
                   seq=client_seq,ack=server_seq)/
               Raw(load=real_get))

client_seq += len(real_get)

# =========================
# 5️⃣ READ IMAGE
# =========================

with open("logo_stego.png","rb") as f:
    image_data = f.read()

key_header = base64.b64encode(b"SOCSECRETKEY2026").decode()

header = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: image/png\r\n"
    "X-Session-Token: " + key_header + "\r\n"
    "X-Encryption: AES-CBC\r\n"
    "\r\n"
).encode()

# Send header
packets.append(IP(src=server,dst=client)/
               TCP(sport=dport,dport=sport,flags="PA",
                   seq=server_seq,ack=client_seq)/
               Raw(load=header))

server_seq += len(header)

# =========================
# 6️⃣ SPLIT IMAGE INTO CHUNKS
# =========================

chunk_size = 100
chunks = [image_data[i:i+chunk_size] for i in range(0,len(image_data),chunk_size)]

for chunk in chunks:
    packets.append(IP(src=server,dst=client)/
                   TCP(sport=dport,dport=sport,flags="PA",
                       seq=server_seq,ack=client_seq)/
                   Raw(load=chunk))
    server_seq += len(chunk)

# =========================
# 7️⃣ EXTRA NOISE POSTS
# =========================

for i in range(4):
    noise = b"POST /api/data HTTP/1.1\r\n\r\nRANDOMDATA"
    packets.append(IP(src=client,dst=server)/
                   TCP(sport=sport,dport=dport,flags="PA",
                       seq=client_seq,ack=server_seq)/
                   Raw(load=noise))
    client_seq += len(noise)

print("Total packets generated:", len(packets))

wrpcap("silent_exfiltration.pcap", packets)

print("[+] Advanced PCAP generated successfully.")
