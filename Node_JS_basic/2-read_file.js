const fs = require('fs');

function countStudents(path) {
	let data;

	try {
		data = fs.readFileSync(path, 'utf8');
	} catch (error) {
		throw new Error('Cannot load the database');
	}

	const lines = data.split('\n').filter((line) => line.trim() !== '');
	const students = lines.slice(1);
	const fields = {};

	for (const student of students) {
		const [firstname, , , field] = student.split(',');

		if (!fields[field]) {
			fields[field] = [];
		}
		fields[field].push(firstname);
	}

	console.log(`Number of students: ${students.length}`);

	for (const field of Object.keys(fields)) {
		const names = fields[field];
		console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
	}
}

module.exports = countStudents;
