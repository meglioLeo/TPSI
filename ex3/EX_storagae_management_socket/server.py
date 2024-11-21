import socket
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

products = []

class Stock:
    
    @staticmethod
    def get_products():  #TODO: Implement this method
        storageFile = open("storage.txt", "r")
        for line in storageFile:
            products.append(line)      
        storageFile.close()
        return products
    
class TCPServer:
    
    def __init__(self, host: str = "0.0.0.0", port: int = 1234):
        self.server_address = (host, port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        try:
            #try to start the server
            self.socket.bind(self.server_address)
            logging.info(f"Server listening on {self.server_address}")
            self.listen()
        except Exception as e:
            #if it fails to start the server
            logging.error(f"Failed to start server: {e}")
        finally:
            #it always does this
            self.socket.close()
            logging.info("Server socket closed.")
            
    def listen(self):
        while True:
            try:
                self.socket.listen(1)
                client_socket, client_address = self.socket.accept()
                logging.info(f"Connection from {client_address}")
                
                data = client_socket.recv(1024)
                request = data.decode("utf-8").strip()
                logging.info(f"Request received: {request}")
                
                if request == "STOCK?":
                    self.handle_stock_request(client_socket)
                else:
                    logging.warning(f"Invalid request: {request}")
            except Exception as e:
                logging.error(f"Error handling client request: {e}")