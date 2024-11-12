import socket
import struct

# Define the NTP server and port
ntp_server = '127.0.0.1'  # Replace with the target NTP server IP address
ntp_port = 123

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# NTP mode 6 query
# Reference: https://tools.ietf.org/html/rfc5905#section-7.3
# Mode 6 is the control message
mode_6_query = b'\x17\x00\x03\x2a' + b'\x00' * 40

try:
    # Send the mode 6 query to the NTP server
    sock.sendto(mode_6_query, (ntp_server, ntp_port))
    
    # Receive the response
    response, _ = sock.recvfrom(1024)
    
    # Print the response
    print("Received response from NTP server:")
    print(response)

except socket.error as e:
    print(f"Socket error: {e}")

finally:
    # Close the socket
    sock.close()
