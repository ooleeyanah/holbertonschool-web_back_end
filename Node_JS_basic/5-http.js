const http = require('http');
const fs = require('fs').promises;

async function getStudentsReport(path) {
	try {
		const data = await fs.readFile(path, 'utf8');
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

		const report = [`Number of students: ${students.length}`];

		for (const field of Object.keys(fields)) {
			report.push(`Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`);
		}

		return report.join('\n');
	} catch (error) {
		throw new Error('Cannot load the database');
	}
}

const app = http.createServer(async (req, res) => {
	res.setHeader('Content-Type', 'text/plain');

	if (req.url === '/') {
		res.statusCode = 200;
		res.end('Hello Holberton School!');
		return;
	}

	if (req.url === '/students') {
		try {
			const report = await getStudentsReport(process.argv[2]);
			res.statusCode = 200;
			res.end(`This is the list of our students\n${report}`);
		} catch (error) {
			res.statusCode = 200;
			res.end(`This is the list of our students\n${error.message}`);
		}
		return;
	}

	res.statusCode = 404;
	res.end('Not found');
});

app.listen(1245);

module.exports = app;
