const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];

  res.setHeader('Content-Type', 'text/plain');
  res.write('This is the list of our students\n');

  countStudents(database)
    .catch(() => {
      res.write('Cannot load the database');
    })
    .finally(() => {
      res.end();
    });
});

app.listen(1245);

module.exports = app;
