# Node.js Basics

## Description

This project introduces the fundamentals of **Node.js** and backend JavaScript development.
You will learn how to execute JavaScript outside the browser, work with modules, build HTTP servers, and use modern development tools like Express, Babel, and Nodemon.


## Objectives

- Running JavaScript using Node.js
- Using Node.js modules
- Reading files with the Node.js `fs` module
- Accessing command-line arguments and environment variables using `process`
- Creating a basic HTTP server using Node.js
- Creating an HTTP server using Express.js
- Building advanced routes with Express.js
- Using ES6 syntax with Babel-node
- Using Nodemon for faster development

## Requirements

- Ubuntu 20.04 LTS
- Node.js installed
- npm installed

## Installation

Clone the repository and install dependencies:

```
git clone <your-repository-url>
cd <your-project-folder>
npm install
```
## Running the Project
Run a JavaScript file with Node.js
```
node filename.js
```

Run with Babel
```
npm run dev
```

Run with Nodemon
```
nodemon filename.js
```

## Project Structure
```
.
├── README.md
├── package.json
├── server.js
├── routes/
├── controllers/
├── utils/
└── tests/
```

## Example: Basic HTTP Server
```
const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200);
  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
```

## Example: Another Basic HTTP Node Server
```
const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

## Example: Express Server
```
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello from Express!');
});

app.listen(1245);

module.exports = app;
```

## Testing

Run tests with:
```
npm test
```
