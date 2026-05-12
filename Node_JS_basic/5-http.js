const http = require('http');
const fs = require('fs');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.write('This is the list of our students\n');

    if (!database) {
      res.end('Cannot load the database');
      return;
    }

    fs.readFile(database, 'utf8', (err, data) => {
      if (err) {
        res.end('Cannot load the database');
        return;
      }

      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);

      const fields = {};

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');

        if (!fields[field]) fields[field] = [];
        fields[field].push(firstname);
      });

      res.write(`Number of students: ${students.length}\n`);

      Object.keys(fields).forEach((field) => {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`,
        );
      });

      res.end();
    });

    return;
  }

  res.end();
});

app.listen(1245);

module.exports = app;
