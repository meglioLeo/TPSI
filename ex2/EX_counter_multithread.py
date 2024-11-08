import threading
import time

class Counter:
    def __init__(self, start_value):
        self.value = start_value
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1
            print(self.value)
            time.sleep(1)

    def decrement(self):
        with self.lock:
            self.value -= 1
            print(self.value)
            time.sleep(1)

counter1 = Counter(0)
counter2 = Counter(11)

threads1 = [threading.Thread(target=counter1.increment) for _ in range(10)]
threads2 = [threading.Thread(target=counter2.decrement) for _ in range(10)]

for t in threads1:
    t.start()

for t in threads2:
    t.start()

for t in threads1:
    t.join()

for t in threads2:
    t.join()