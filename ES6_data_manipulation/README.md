ES6 data manipulation
# JavaScript Data Structures & Array Methods Guide

This README explains how to use some of the most important JavaScript array methods and built-in data structures:

- map, filter, reduce
- Typed Arrays
- Set, Map, WeakMap, WeakSet

---

# 1. Array Methods

JavaScript provides powerful methods to work with arrays in a functional way.

## map()

Ttransforms each element in an array and returns a new array.

### Example:
```
const numbers = [1, 2, 3];

const doubled = numbers.map(n => n * 2);

console.log(doubled); // [2, 4, 6]
```
Use case:
Transforming data, Formatting values

## filter()

Returns a new array with elements that match a condition.

```
const numbers = [1, 2, 3, 4, 5];

const evenNumbers = numbers.filter(n => n % 2 === 0);

console.log(evenNumbers); // [2, 4]
```
Use case:
Removing unwanted items, searching data

## reduce()

Combines all array elements into a single value.

Sum of numbers:
```
const numbers = [1, 2, 3, 4];

const sum = numbers.reduce((acc, curr) => acc + curr, 0);

console.log(sum); // 10
```

Count occurrences
```
const fruits = ["apple", "banana", "apple"];

const count = fruits.reduce((acc, fruit) => {
  acc[fruit] = (acc[fruit] || 0) + 1;
  return acc;
}, {});

console.log(count); // { apple: 2, banana: 1 }
```
Use case: Summing values, grouping data, converting arrays into objects

## Typed Arrays

Typed Arrays provide a way to handle binary data efficiently in JavaScript.

They are used in:

- Graphics (WebGL)
- Audio/Video processing
- File manipulation
- Performance-sensitive applications
```
const buffer = new ArrayBuffer(16);
const view = new Int32Array(buffer);

view[0] = 100;
view[1] = 200;

console.log(view); // Int32Array(4) [100, 200, 0, 0]
```

### Common Typed Arrays:
```
Type	        Description

Int8Array	    8-bit signed integers
Uint8Array	    8-bit unsigned integers
Int16Array	    16-bit signed integers
Int32Array	    32-bit signed integers
Float32Array	32-bit floating numbers
Float64Array	64-bit floating numbers
```
## Set, Map, WeakMap, WeakSet

These are modern JavaScript data structures used for storing collections of data.

### Set

A Set stores unique values only.

```
const set = new Set();

set.add(1);
set.add(2);
set.add(2);

console.log(set); // Set { 1, 2 }
```

Use case: removing duplicates, tracking unique items

## Map

A Map stores key-value pairs and allows any type of key.

```
const map = new Map();

map.set("name", "Alice");
map.set(1, "number key");

console.log(map.get("name")); // Alice
```

Use case: better key-value storage than objects, when keys are not just strings

## WeakMap

A WeakMap is like a Map but:

- Keys must be objects
- Keys are weakly referenced (can be garbage collected)
```
let obj = {};

const weakMap = new WeakMap();
weakMap.set(obj, "secret data");

obj = null; // memory can now be cleaned up
```
Use case: private data storage, memory-efficient caching

## WeakSet

A WeakSet only stores objects and allows garbage collection.

```
let obj = {};

const weakSet = new WeakSet();
weakSet.add(obj);
```
Use case: tracking object existence without preventing garbage collection

## Summary
```
Feature	            Purpose

map()	            Transform arrays
filter()	        Select elements
reduce()	        Combine into one value
Typed Arrays	    Efficient binary data handling
Set                 Unique values
Map                 Key-value pairs
WeakMap / WeakSet	Memory-safe object storage
```