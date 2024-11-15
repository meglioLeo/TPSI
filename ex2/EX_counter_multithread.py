import threading
import time

sem = threading.Semaphore(0)  # Create a semaphore with an initial value of 0

class Counter:
    def __init__(self, start_value):
        self.value = start_value      # Initialize the value that will be changed by the threads
        self.lock = threading.Lock()  # Create a lock object to synchronize access to the shared resource

    def increment(self):
        with self.lock:
            for i in range(10):
                self.value += 1
                print(f"Incrementing thread: {self.value}")
                time.sleep(1)   # Simulate a delay to make the thread execution slower
        sem.release()

    def decrement(self):
        with self.lock:
            sem.acquire()
            for i in range(10):
                self.value -= 1     
                print(f"Decrementing thread: {self.value}")
                time.sleep(1)   # Simulate a delay to make the thread execution slower

counter1 = Counter(0)   
counter2 = Counter(11)  

thread1 = threading.Thread(target=counter1.increment)     # Create a thread that will increment the counter
thread2 = threading.Thread(target=counter2.decrement)

thread1.start()   # Start the thread
thread2.start()

thread1.join()    # Wait for the thread to finish
thread2.join()