import threading
import time

class Block:
    def __init__(self):
        self.value = 1
        
    def calculate(self):
        for i in range(1000000):
            self.value += 1
            
    