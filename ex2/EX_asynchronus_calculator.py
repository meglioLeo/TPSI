import asyncio

async def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        await asyncio.sleep(1) #Simulate a delay
    print(f"Calculated factorial of {n} and the result is {result}")
    return result

async def main():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10]
    tasks = [factorial(n) for n in numbers]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")
    
asyncio.run(main())