import threading
import asyncio

def factorial(n):
    if n == 0:
        print(f"Thread {threading.current_thread().name} calculated factorial of {n} and the result is 1")
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"Thread {threading.current_thread().name} calculated factorial of {n} and the result is {result}")
    return result

async def main():
    threads = [threading.Thread(target = lambda: factorial(10),) for _ in range(10)]    #lambda allows to create anonymous functions
    
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
asyncio.run(main())