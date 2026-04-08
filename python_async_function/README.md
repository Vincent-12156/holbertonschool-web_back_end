# Python - Async
## Asyncio and Random Module in Python

This README covers:

- async and await syntax
- Executing an async program with asyncio
- Running concurrent coroutines
- Creating asyncio tasks
- Using the random module

### 1. async and await Syntax

Python allows you to write asynchronous code using async and await.

- async def defines an asynchronous function (coroutine).
- await pauses the coroutine until the awaited coroutine or Future is done.
import asyncio
```
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```

### 2. Executing an Async Program with asyncio

The recommended way to run async programs is using asyncio.run():
```
async def main():
    print("Starting async program")
    await asyncio.sleep(1)
    print("Async program finished")

asyncio.run(main())
```

### 3. Running Concurrent Coroutines

asyncio.gather() allows multiple coroutines to run concurrently:
```
async def task1():
    await asyncio.sleep(1)
    return "Task 1 done"

async def task2():
    await asyncio.sleep(2)
    return "Task 2 done"

async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())
```
Output will be roughly after 2 seconds (both run concurrently):
```
['Task 1 done', 'Task 2 done']
```

### 4. Creating asyncio Tasks

Tasks allow you to schedule coroutines concurrently:
```
async def my_coroutine(name, delay):
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} seconds")

async def main():
    task_a = asyncio.create_task(my_coroutine("A", 2))
    task_b = asyncio.create_task(my_coroutine("B", 1))
    
    await task_a
    await task_b

asyncio.run(main())
```
Output (order depends on delay):
```
B finished after 1 seconds
A finished after 2 seconds
```

### 5. Using the random Module

The random module is useful for generating random numbers, choices, or shuffling data.
```
import random

# Random integer between 1 and 10
num = random.randint(1, 10)
print("Random integer:", num)

# Random float between 0 and 1
flt = random.random()
print("Random float:", flt)

# Random choice from a list
colors = ["red", "green", "blue"]
choice = random.choice(colors)
print("Random color:", choice)

# Shuffle a list
random.shuffle(colors)
print("Shuffled colors:", colors)
```

### 6. Combining asyncio with random

You can combine async coroutines with random delays:
```
async def random_task(name):
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"{name} finished after {delay} seconds")

async def main():
    tasks = [asyncio.create_task(random_task(f"Task {i}")) for i in range(5)]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

This demonstrates concurrency with unpredictable delays.