import socket
import struct
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TCPclient:

    def __init__(self, serevr_host: str, server_port: int, timeout: float = 1.0):
        self.server_address = (serevr_host, server_port)
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)

    def send_request(self, message: str):
        #TODO implement this metod