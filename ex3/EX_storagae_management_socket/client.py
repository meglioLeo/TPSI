import socket
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class TCPClient:
    def __init__(self, server_host: str, server_port: int, timeout: float = 1.0):
        self.server_address = (server_host, server_port)
        self.timeout = timeout
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)

    def send_request(self, message: str):
        try:
            self.socket.connect(self.server_address)
            logging.info(f"Sending request to {self.server_address}: {message}")
            self.socket.sendall(message.encode("utf-8"))
            
            response = self.socket.recv(1024).decode("utf-8")
            logging.info(f"Response received: {response}")

            # Decodifica risposta STOCK?
            if message == "STOCK?":
                print("Stock data:")
                print(response)
            elif message.startswith("MODIFY_QUANTITY?"):
                print("Modification response:")
                print(response)
        except socket.timeout:
            logging.error("No response received within the timeout period.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            self.socket.close()


if __name__ == "__main__":
    client = TCPClient(server_host="localhost", server_port=1234)
    client.send_request("STOCK?")  # Richiesta elenco prodotti
    client.send_request("MODIFY_QUANTITY?101,50")  # Modifica quantità prodotto
