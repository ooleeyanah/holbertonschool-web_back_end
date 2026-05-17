import readDatabase from '../utils';

export default class StudentsController {
	static getAllStudents(req, res) {
		readDatabase(process.argv[2])
			.then((studentsByField) => {
				const fields = Object.keys(studentsByField).sort((a, b) => a.localeCompare(b, undefined, { sensitivity: 'base' }));
				const lines = ['This is the list of our students'];

				fields.forEach((field) => {
					lines.push(`Number of students in ${field}: ${studentsByField[field].length}. List: ${studentsByField[field].join(', ')}`);
				});

				res.status(200).send(lines.join('\n'));
			})
			.catch(() => {
				res.status(500).send('Cannot load the database');
			});
	}

	static getAllStudentsByMajor(req, res) {
		const { major } = req.params;

		if (major !== 'CS' && major !== 'SWE') {
			res.status(500).send('Major parameter must be CS or SWE');
			return;
		}

		readDatabase(process.argv[2])
			.then((studentsByField) => {
				const students = studentsByField[major] || [];
				res.status(200).send(`List: ${students.join(', ')}`);
			})
			.catch(() => {
				res.status(500).send('Cannot load the database');
			});
	}
}
