import fs from 'fs';

export default function readDatabase(filePath) {
	return new Promise((resolve, reject) => {
		fs.readFile(filePath, 'utf-8', (error, data) => {
			if (error) {
				reject(error);
				return;
			}

			const lines = data
				.split('\n')
				.filter((line) => line.trim() !== '');
			const studentsByField = {};

			lines.slice(1).forEach((line) => {
				const [firstName, , , field] = line.split(',');

				if (!studentsByField[field]) {
					studentsByField[field] = [];
				}

				studentsByField[field].push(firstName);
			});

			resolve(studentsByField);
		});
	});
}
