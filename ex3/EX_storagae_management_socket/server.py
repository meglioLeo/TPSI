import socket
import logging
import struct

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Stock:
    @staticmethod
    def get_products():
        products = {}
        with open("storage.txt", "r") as storageFile:
            for line in storageFile:
                product_id, name, quantity = line.strip().split(",")
                products[int(product_id)] = {"name": name, "quantity": int(quantity)}
        return products

    @staticmethod
    def save_products(products):
        with open("storage.txt", "w") as storageFile:
            for product_id, details in products.items():
                storageFile.write(f"{product_id},{details['name']},{details['quantity']}\n")


class TCPServer:
    def __init__(self, host: str = "0.0.0.0", port: int = 1234):
        self.server_address = (host, port)
        self.buffer_size = 1024
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        try:
            self.socket.bind(self.server_address)
            logging.info(f"Server listening on {self.server_address}")
            self.listen()
        except Exception as e:
            logging.error(f"Failed to start server: {e}")
        finally:
            self.socket.close()
            logging.info("Server socket closed.")
            
    def listen(self):
        while True:
            try:
                self.socket.listen(1)
                client_socket, client_address = self.socket.accept()
                logging.info(f"Connection from {client_address}")
                
                data = client_socket.recv(self.buffer_size)
                request = data.decode("utf-8").strip()
                logging.info(f"Request received: {request}")
                
                if request == "STOCK?":
                    self.handle_stock_request(client_socket)
                elif request.startswith("MODIFY_QUANTITY?"):
                    self.handle_modify_quantity_request(client_socket, request)
                else:
                    client_socket.sendall(b"Invalid request")
            except Exception as e:
                logging.error(f"Error handling client request: {e}")

    def handle_stock_request(self, client_socket):
        """
        Gestisce la richiesta STOCK?.
        """
        try:
            products = Stock.get_products()
            response = "\n".join(
                [f"{product_id},{details['name']},{details['quantity']}" for product_id, details in products.items()]
            )
            client_socket.sendall(response.encode("utf-8"))  # Risponde con i prodotti
            logging.info("Sent stock data to client.")
        except Exception as e:
            logging.error(f"Error sending stock data: {e}")

    def handle_modify_quantity_request(self, client_socket, request):
        """
        Gestisce la richiesta MODIFY_QUANTITY?.
        """
        try:
            parts = request.split("?")[1].strip().split(",")
            if len(parts) != 2:
                client_socket.sendall(b"Invalid MODIFY_QUANTITY format")
                return

            product_id, new_quantity = int(parts[0]), int(parts[1])
            products = Stock.get_products()

            if product_id in products:
                products[product_id]["quantity"] = new_quantity
                Stock.save_products(products)
                client_socket.sendall(b"Quantity updated successfully")
                logging.info(f"Updated product {product_id} to {new_quantity}")
            else:
                client_socket.sendall(b"Product not found")
        except Exception as e:
            logging.error(f"Error handling MODIFY_QUANTITY: {e}")
            client_socket.sendall(b"Error updating quantity")


if __name__ == "__main__":
    server = TCPServer(host="localhost", port=1234)
    server.start()