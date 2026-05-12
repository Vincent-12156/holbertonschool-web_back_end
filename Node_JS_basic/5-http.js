const http = require("http");
const countStudents = require("./3-read_file_async");

const app = http.createServer((req, res) => {
  const { url } = req;

  res.writeHead(200, { "Content-Type": "text/plain" });

  if (url === "/") {
    res.end("Hello Holberton School!");
  } else if (url === "/students") {
    const database = process.argv[2];

    res.write("This is the list of our students\n");

    countStudents(database)
      .then(() => {
        res.end();
      })
      .catch(() => {
        res.end("Cannot load the database");
      });
  } else {
    res.end("Hello Holberton School!");
  }
});

app.listen(1245);

module.exports = app;
