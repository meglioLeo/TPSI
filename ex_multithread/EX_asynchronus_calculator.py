import asyncio

async def factorial(n):  #This function is a coroutine that calculates the factorial of a number
    result = 1
    for i in range(1, n+1):
        result *= i
        await asyncio.sleep(1) #Simulate a delay
    print(f"Calculated factorial of {n} and the result is {result}")
    return result

async def main():   #This function is a coroutine that creates a list of tasks and waits for them to finish
    numbers = [3, 4, 5, 6, 7, 8, 9, 10]   #List of numbers to calculate the factorial
    tasks = [factorial(n) for n in numbers]   #Create a list of tasks
    results = await asyncio.gather(*tasks)    #Wait for all tasks to finish and get the results
    print(f"Results: {results}")
    
asyncio.run(main())    #Run the main coroutine