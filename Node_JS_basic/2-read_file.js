const fs = require("fs");

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, "utf8");
    const lines = data.trim().split("\n");

    const students = {};

    for (let i = 1; i < lines.length; i += 1) {
      if (lines[i].trim() === "") continue;

      const [firstname, , , field] = lines[i].split(",");

      if (!students[field]) {
        students[field] = [];
      }
      students[field].push(firstname);
    }

    console.log(
      `Number of students: ${Object.values(students).reduce((a, b) => a + b.length, 0)}`,
    );

    for (const [field, list] of Object.entries(students)) {
      console.log(
        `Number of students in ${field}: ${list.length}. List: ${list.join(", ")}`,
      );
    }
  } catch (err) {
    throw new Error("Cannot load the database");
  }
}

module.exports = countStudents;
