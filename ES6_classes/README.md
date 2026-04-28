# Classes and Advanced Concepts in ES6

## How to define a Class  
In ES6, a class is a blueprint used to create objects with shared properties and methods.

```
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
}
```
You can create an instance of the class using new:
```
const user = new Person("Alice", 25);
```

## How to add methods to a class

Methods are functions defined inside a class. They are shared by all instances of that class.
```
class Person {
  constructor(name) {
    this.name = name;
  }

  greet() {
    return `Hello, my name is ${this.name}`;
  }
}

const user = new Person("Alice");
console.log(user.greet());
```
## Why and how to add a static method to a class

A static method belongs to the class itself, not to instances. It is useful for utility functions related to the class.
```
class MathHelper {
  static add(a, b) {
    return a + b;
  }
}

console.log(MathHelper.add(2, 3)); // 5
```
Use static methods when the function does not need instance-specific data.

## How to extend a class from another

You can create a new class based on an existing one using extends. This is called inheritance.
```
class Person {
  constructor(name) {
    this.name = name;
  }
}

class Student extends Person {
  constructor(name, grade) {
    super(name); // call parent constructor
    this.grade = grade;
  }

  study() {
    return `${this.name} is studying`;
  }
}

const student = new Student("Alice", "A");
```
super() is used to access the parent class constructor or methods.

## Metaprogramming and symbols
### Symbols

A Symbol is a unique and immutable value, often used as object property keys to avoid conflicts.
```
const id = Symbol("id");

const user = {
  name: "Alice",
  [id]: 123
};
```
Each symbol is unique, even if they have the same description.

### Metaprogramming

Metaprogramming means writing code that can manipulate other code or itself.

In ES6, this is often done using:

- Symbol (custom object behavior)
- Reflect (methods to interact with objects)
- Proxy (intercept and customize operations)

Example with Proxy:
```
const user = {
  name: "Alice"
};

const proxy = new Proxy(user, {
  get(target, prop) {
    return prop in target ? target[prop] : "Property not found";
  }
});

console.log(proxy.name); // Alice
console.log(proxy.age);  // Property not found
```
This allows you to control how objects behave dynamically.
