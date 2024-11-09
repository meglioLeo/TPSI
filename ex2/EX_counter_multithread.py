import threading
import time

class Counter:
    def __init__(self, start_value):
        self.value = start_value
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            for i in range(10):
                self.value += 1
                print(self.value)
                time.sleep(1)

    def decrement(self):
        with self.lock:
            for i in range(10):
                self.value -= 1
                print(self.value)
                time.sleep(1)

counter1 = Counter(0)
counter2 = Counter(11)

thread1 = threading.Thread(target=counter1.increment)
thread2 = threading.Thread(target=counter2.decrement)

thread1.start()

thread2.start()

thread1.join()

thread2.join()