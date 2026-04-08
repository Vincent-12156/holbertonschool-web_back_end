# Python - Variable Annotations
## Type Annotations in Python 3

Type annotations (also called type hints) are a way to specify the expected data types of variables, function parameters, and return values in Python. They were introduced in Python 3 to improve code readability and enable static type checking.

Unlike some other languages, Python does not enforce types at runtime by default. Instead, type annotations are mainly used by developers and external tools.

## How you can use type annotations to specify function signatures and variable types

Type annotations can be added using a colon `:` for variables and parameters, and `->` for return types.

## Function annotations

```
def greet(name: str) -> str:
    return f"Hello, {name}"
```
 - name: str indicates that name should be a string
 - -> str indicates the function returns a string

### Multiple parameters
```
def add(a: int, b: int) -> int:
    return a + b
```
### Variable annotations
```
age: int = 25
price: float = 19.99
name: str = "Alice"
```
### Using complex types
```
from typing import List, Dict

numbers: List[int] = [1, 2, 3]
user: Dict[str, str] = {"name": "Alice", "city": "Paris"}
```
### Optional and default values
```
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello!"
    return f"Hello, {name}"
```

## Duck typing

Duck typing is a concept in Python where the type of an object is determined by its behavior (methods and properties) rather than its actual class.

“If it looks like a duck and quacks like a duck, it’s a duck.”

### Example of duck typing
```
class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

def make_sound(animal):
    return animal.speak()

print(make_sound(Dog()))
print(make_sound(Cat()))
```
 - The function make_sound does not care about the object's type
 - It only requires that the object has a .speak() method

### Duck typing with type hints

You can make duck typing more explicit using protocols:
```
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        ...

def make_sound(animal: Speaker) -> str:
    return animal.speak()
```

### How to validate your code with mypy

mypy is a static type checker for Python that helps catch type-related errors before running your code.

 - Installation
```
pip install mypy
```
 - Running mypy
```
mypy your_script.py
```
 - Example
```
def add(a: int, b: int) -> int:
    return a + b

result = add(1, "2")  # This is incorrect
```

Running mypy:
```
mypy example.py
```
Output:
```
error: Argument 2 to "add" has incompatible type "str"; expected "int"
```
Benefits of using mypy
Detects type errors early
Improves code quality and maintainability
Makes large codebases easier to understand
Works well with IDEs and CI pipelines
