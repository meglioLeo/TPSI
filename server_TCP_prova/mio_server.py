import socket

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind(('localhost', 12345))
socket_server.listen(5)  

while True:
    client_socket, address = socket_server.accept()
    print(f"Connection from {address} has been established!")
    message = client_socket.recv(1024).decode()
    print(f"Message from client: {message}")
    client_socket.send("Message received!".encode())
    client_socket.close()