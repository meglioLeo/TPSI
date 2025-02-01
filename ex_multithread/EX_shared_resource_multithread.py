import threading
import time

class Counter:
    def __init__(self):
        self.value = 1
        self.lock = threading.Lock()
        
    def increment(self, thread_namae):
        with self.lock:
            self.value = self.value * 1000   #Simulate a long running calculation
            print(f"{thread_namae} incremented counter to: {self.value}")
            time.sleep(0.5)   #Simulate a delay to show the effect of multithreading
                
shared_counter = Counter()

#Create a list of 10 threads                
threads = [threading.Thread(target=shared_counter.increment, args=(f"thread {i+1}",)) for i in range(10)]  

for t in threads:
    t.start()
    
for t in threads:
    t.join()