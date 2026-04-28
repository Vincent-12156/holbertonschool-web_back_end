# Python - Async Comprehension
## 1- How to write an asynchronous generator

An asynchronous generator is like a normal generator (yield) but works with async / await.

### Basic example
```
import asyncio

async def async_counter():
    for i in range(3):
        await asyncio.sleep(1)  # simulate async work
        yield i
```
### How to consume it

You must use async for:
```
async def main():
    async for value in async_counter():
        print(value)

asyncio.run(main())
```
### Key rules
 - Defined with async def
 - Uses yield (not return for values)
 - Consumed with async for
 - Can use await inside

## 2- How to use async comprehensions

Async comprehensions let you build collections from async iterables.

### Example
```
async def async_counter():
    for i in range(5):
        yield i

async def main():
    result = [x async for x in async_counter()]
    print(result)

# Output: [0, 1, 2, 3, 4]
```
### With filtering
```
result = [x async for x in async_counter() if x % 2 == 0]
```
### Works with other structures too
```
# set
result = {x async for x in async_counter()}

# dict
result = {x: x*x async for x in async_counter()}
```
### Important constraint

You can only use async comprehensions inside an async function.

## 3- How to type-annotate generators

Use the typing module.

### A. Regular generators
```
from typing import Generator

def count() -> Generator[int, None, None]:
    yield 1
    yield 2
		```

 - Generator type format:
```
Generator[yield_type, send_type, return_type]
```
Example with send():
```
def echo() -> Generator[int, int, None]:
    value = yield 1
    yield value
		```
### B. Async generators
Use AsyncGenerator:
```
from typing import AsyncGenerator

async def async_counter() -> AsyncGenerator[int, None]:
    for i in range(3):
        yield i
```
 - Format:
 ```
AsyncGenerator[yield_type, send_type]
```
### C. When to use Iterator / AsyncIterator
Sometimes simpler:
```
from typing import Iterator, AsyncIterator

def gen() -> Iterator[int]:
    yield 1

async def agen() -> AsyncIterator[int]:
    yield 1
```
Use:

 - Iterator → when you don’t care about .send()
 - AsyncIterator → same idea for async

## Comparison
| Type                 | Syntax                   | Consumption   |
|----------------------|--------------------------|---------------|
| Generator            | `def` + `yield`          | `for`         |
| Async Generator      | `async def` + `yield`    | `async for`   |
| Async comprehension  | `[x async for x in ...]` | inside `async`|