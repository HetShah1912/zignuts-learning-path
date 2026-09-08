// Task 3: Write a JavaScript program that creates a class called 'Shape' with a method to
// calculate the area. Create two subclasses, 'Circle' and 'Triangle', that inherit from the
// 'Shape' class and override the area calculation method. Create an instance of the 'Circle'
// class and calculate its area. Similarly, do the same for the 'Triangle' class.

class Shape{
  constructor(){
    console.log("Shape Created")
  }
  area() {
    return 0;
  }
}

class Triangle extends Shape{
  constructor(base, height) {
    super();
    console.log("Shape : Triangle");
    this.base = base;
    this.height = height;
  }
  area() {
    return 0.5 * this.base * this.height;
  }
}

class Circle extends Shape{
  constructor(radius){
    super();
    console.log("Shape : Circle");
    this.radius = radius;
  }
  area() {
    return Math.PI * this.radius * this.radius;
  }
}

const t1 = new Triangle(3,2);
console.log(t1.area());
const c1 = new Circle(6);
console.log(c1.area());