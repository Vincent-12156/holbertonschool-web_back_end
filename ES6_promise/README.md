ES6 Promises

# JavaScript Async Programming (Promises & async/await)

This project covers modern asynchronous programming in JavaScript using:

- Promises
- .then(), .catch(), Promise.resolve()
- Promise.all, Promise.race, Promise.allSettled, Promise.any
- try / catch error handling
- async / await

These tools are essential for handling operations like API calls, file reading, and any non-blocking tasks in JavaScript.

## Promises: What, Why, How
### What is a Promise?
A Promise is an object representing the eventual completion (or failure) of an asynchronous operation.

A Promise has 3 states:

- pending
- fulfilled
- rejected

### Why use Promises?
- Avoid callback hell
- Handle async code more cleanly
- Better error handling
- Easier chaining of operations

### How to create a Promise
```
const myPromise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Operation successful");
  } else {
    reject("Something went wrong");
  }
});
```

## Using .then(), .catch(), and resolve
### .then()
Handles successful resolution:
```
myPromise.then((result) => {
  console.log(result);
});
```

### .catch()
Handles errors:
```
myPromise.catch((error) => {
  console.error(error);
});
```

### Chaining
```
myPromise
  .then((result) => {
    return result + "!";
  })
  .then((newResult) => {
    console.log(newResult);
  })
  .catch((error) => {
    console.error(error);
  });
```

## Promise Methods
- Promise.resolve()

Creates an already resolved promise:
```
Promise.resolve("Success").then(console.log);
```

- Promise.reject()

Creates an already rejected promise:
```
Promise.reject("Error").catch(console.error);
```

- Promise.all()

Waits for all promises to resolve (fails if one fails):
```
Promise.all([p1, p2, p3]).then((values) => {
  console.log(values);
});
```

- Promise.race()

Returns the first promise that settles:
```
Promise.race([p1, p2]).then(console.log);
```

- Promise.allSettled()

Waits for all promises, regardless of success/failure:
```
Promise.allSettled([p1, p2]).then(console.log);
```

- Promise.any()

Returns the first fulfilled promise:
```
Promise.any([p1, p2]).then(console.log);
```

## Throw / Try / Catch

Used for synchronous and async error handling.
```
try {
  throw new Error("Something failed");
} catch (error) {
  console.error(error.message);
}
```

### Async / Await
What is async/await?

A modern way to write asynchronous code that looks synchronous.

- async function
```
async function myFunction() {
  return "Hello";
}
```
This automatically returns a Promise.

- await operator

Waits for a Promise to resolve:
```
async function fetchData() {
  const result = await myPromise;
  console.log(result);
}
```

Example with error handling
```
async function getData() {
  try {
    const data = await fetch("https://api.example.com");
    const json = await data.json();
    console.log(json);
  } catch (error) {
    console.error(error);
  }
}
```

## Key Takeaways
- Promises handle async operations cleanly
- .then() handles success, .catch() handles errors
- Promise.* methods help coordinate multiple async tasks
- async/await makes asynchronous code easier to read
- Always use try/catch with await for error handling

## Summary
```
Concept	    Purpose

Promise     Represents async result
then	    Handle success
catch	    Handle error
async	    Define async function
await	    Pause until promise resolves
try/catch	Error handling
```