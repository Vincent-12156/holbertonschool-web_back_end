const fs = require("fs");

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf8", (err, data) => {
      if (err) {
        reject(new Error("Cannot load the database"));
        return;
      }

      const lines = data.toString().trim().split("\n");

      const students = {};

      for (let i = 1; i < lines.length; i += 1) {
        if (lines[i].trim() === "") continue;

        const [firstname, , , field] = lines[i].split(",");

        if (!students[field]) {
          students[field] = [];
        }
        students[field].push(firstname);
      }

      const total = Object.values(students).reduce(
        (acc, list) => acc + list.length,
        0,
      );

      console.log(`Number of students: ${total}`);

      for (const [field, list] of Object.entries(students)) {
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(", ")}`,
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
