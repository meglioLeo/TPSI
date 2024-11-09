import threading
import time

class Block:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
        
    def calculate(self):
        for i in range(1000001):
            with self.lock:
                self.value = self.value + i
    
    def print_status(self, thread_name):
        while thread_name.is_alive():
            with self.lock:
                print(self.value)
                time.sleep(0.5)
        print(f"Final value: {self.value}")
            
block = Block()

thread1 = threading.Thread(target=block.calculate)
thread2 = threading.Thread(target=block.print_status, args=(thread1,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()  