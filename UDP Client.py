import socket

target_host = '127.0.0.1'  # Change to your target IP
target_port = 80  # Make sure the server is listening on this port

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send some data (encode string to bytes)
message = b"AABBCC"
client.sendto(message, (target_host, target_port))

# Receive some data
data, addr = client.recvfrom(4096)  # Receive up to 4096 bytes

# Print received data (decode for readability)
print("Received:", data.decode(errors="ignore"))

# Close the socket
client.close()
