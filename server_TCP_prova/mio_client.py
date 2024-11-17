import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_socket.send("Hello, server!".encode())
response = client_socket.recv(1024).decode()
print(f"Serever response: {response}")
client_socket.close()