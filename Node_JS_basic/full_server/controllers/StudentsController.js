const readDatabase = require("../utils");

class StudentsController {
  static getAllStudents(req, res) {
    const dbFile = process.argv[2];

    readDatabase(dbFile)
      .then((data) => {
        res.status(200);
        res.write("This is the list of our students\n");

        const keys = Object.keys(data).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase()),
        );

        keys.forEach((field) => {
          const list = data[field];
          res.write(
            `Number of students in ${field}: ${list.length}. List: ${list.join(", ")}\n`,
          );
        });

        res.end();
      })
      .catch(() => {
        res.status(500).send("Cannot load the database");
      });
  }

  static getAllStudentsByMajor(req, res) {
    const dbFile = process.argv[2];
    const { major } = req.params;

    if (major !== "CS" && major !== "SWE") {
      res.status(500).send("Major parameter must be CS or SWE");
      return;
    }

    readDatabase(dbFile)
      .then((data) => {
        const list = data[major] || [];
        res.status(200).send(`List: ${list.join(", ")}`);
      })
      .catch(() => {
        res.status(500).send("Cannot load the database");
      });
  }
}

module.exports = StudentsController;
