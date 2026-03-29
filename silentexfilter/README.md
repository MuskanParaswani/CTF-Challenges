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
