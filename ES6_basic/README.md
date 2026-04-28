# Learning Objectives

## What ES6 is  
ES6 (ECMAScript 2015) is a version of JavaScript designed to make the language easier to use, more consistent, and more powerful. It introduced modern syntax and features that help developers write cleaner and more maintainable code.



## New features introduced in ES6  
Some of the main features introduced in ES6 include:
- `let` and `const` for variable declaration  
- Arrow functions  
- Template literals  
- Default parameters  
- Rest and spread operators  
- Object shorthand syntax  
- Classes  
- Modules (`import` / `export`)  
- Iterators and `for...of` loops  



## The difference between a constant and a variable  
A variable can be modified after its declaration, while a constant cannot be reassigned.

```
let a = 1;  
const b = 2;  

a = 3; # Works  
b = 4; # Don't work 
```

## Block-scoped variables

A block-scoped variable is declared inside a block ({}) and can only be accessed within that block.
```
if (true) {
  let x = 10;
  const y = 20;
}

x and y are not accessible here
```
This is different from var, which is function-scoped.

## Arrow functions and function parameters default to them

Arrow functions provide a shorter and cleaner way to write functions.

```
const add = (a, b) => a + b;
console.log(add(5, 3)); // 8
```
They also support default parameters:
```
const greet = (name = "Guest") => `Hello, ${name}`;
```
## Rest and spread function parameters

The spread operator (...) expands elements from arrays or objects:
```
const numbers = [1, 2, 3];
const newNumbers = [...numbers, 4, 5];
```
The rest operator (...) collects multiple values into an array:
```
const sum = (...nums) => nums.reduce((acc, n) => acc + n, 0);
```
## String templating in ES6

Template literals allow you to create dynamic strings using backticks (`) and ${}.
```
console.log(`Hello, ${1 + 1} is the answer!`);
```
They also allow multi-line strings:
```
const text = `Line 1
Line 2`;
```
## Object creation and their properties in ES6

ES6 makes object creation simpler with shorthand syntax.
```
const name = "Alice";
const age = 25;

const user = {
  name,
  age,
  greet() {
    console.log("Hello!");
  }
};
```
You can also use computed property names:
```
const key = "score";

const obj = {
  [key]: 100
};
```
## Iterators and for-of loops

Iterators allow you to go through collections like arrays, strings, and more.

The for...of loop makes it easy to iterate over values:
```
const arr = [1, 2, 3];

for (const value of arr) {
  console.log(value);
}
```
Iterates over values, unlike for...in, which iterates over indexes/keys.
