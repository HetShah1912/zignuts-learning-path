// Task 4: Write a JavaScript program that creates a class called University with properties
// for university names and departments. Include methods to add a department, remove a
// department, and display all departments. Create an instance of the University class and
// add and remove departments.

class University {
  constructor(uni_name) {
    this.uni_name = uni_name;
    this.departments = [];
  }

  add_department(dept_name) {
    this.departments.push(dept_name);
  }

  remove_department(dept_name) {
    this.departments = this.departments.filter((department) => department !== dept_name);
  }

  display_departments() {
    let no = 1;
    console.log("University : " + this.uni_name);
    this.departments.forEach((department) => {
      console.log(no + " : " + department + " Department");
      no++;
    })
  }
}

const uni1 = new University("Indus University");
uni1.add_department("Computer Science");
uni1.add_department("Information Technology");
uni1.add_department("Mechanical");
uni1.add_department("Civil");
uni1.display_departments();

uni1.remove_department("Civil");
uni1.display_departments();



