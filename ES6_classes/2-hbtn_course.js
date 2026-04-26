export default class HolbertonCourse {
    constructor(name, length, students) {
        name = "";
        length = 0;
        students = [""];
        this._name = name;
        this._length = length;
        this._students = students;
    }
    get name() {
        return this._name;
    }
    get length() {
        return this._length;
    }
    get students() {
        return this._students;
    }
    set name(newName) {
        if (newName.length > 0) {
            this._name = newName;
        } else {
            console.error("Name cannot be empty!");
        }
    }
    set length(newLength) {
        if (newLength.length > 0) {
            this._length = newLength;
        } else {
            console.error("Length cannot be zero!");
        }
    }
    set students(newStudents) {
        if (newStudents > 0) {
            this._students = newStudents;
        } else {
            console.error("You need at least one student!");
        }
    }
}