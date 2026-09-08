// Data Types
console.log("---Data types---");

// Number
let numberLength = 16;
let numberWeight = 7.5;

// BigInt
let bigIntX = 1234567890123456789012345n;
let bigIntY = BigInt("1234567890123456789012345");

// Strings
let stringColor = "Yellow";
let stringLastName = "Johnson";

// Boolean
let booleanTrue = true;
let booleanFalse = false;

// Undefined
let undefinedX;
let undefinedY;

// Null
let nullX = null;
let nullY = null;

// Symbol
const symbolX = Symbol();
const symbolY = Symbol();

// Object
const personObject = {
  firstName: "John",
  lastName: "Doe"
};

// Array Object
const carsArray = ["Saab", "Volvo", "BMW"];

// Date Object
const dateObject = new Date("2026-09-06");


// Printing all variables
console.log("Number Length:", numberLength);
console.log("Number Weight:", numberWeight);

console.log("BigInt X:", bigIntX);
console.log("BigInt Y:", bigIntY);

console.log("String Color:", stringColor);
console.log("String Last Name:", stringLastName);

console.log("Boolean True:", booleanTrue);
console.log("Boolean False:", booleanFalse);

console.log("Undefined X:", undefinedX);
console.log("Undefined Y:", undefinedY);

console.log("Null X:", nullX);
console.log("Null Y:", nullY);

console.log("Symbol X:", symbolX);
console.log("Symbol Y:", symbolY);

console.log("Person Object:", personObject);

console.log("Cars Array:", carsArray);
console.log("Date Object:", dateObject);

// Operators

// Assignment
console.log("---Assignment Operators---");
let x = 10;
let y = 20;
x += y;
console.log(x);
x -= y;
console.log(x);
x *= y;
console.log(x);
x **= y;
console.log(x);
x /= y;
console.log(x);
x %= y;
console.log(x);

// Arithmatic
console.log("---Arithmatic Operators---");
console.log(x + y);
console.log(x - y);
console.log(x * y);
console.log(x / y);
console.log(x ** y);
console.log(x % y);

// Logical
console.log("---Logical Operators---");
// AND
let logicalAndX = true;
let logicalAndy = logicalAndX &&= 10;
console.log(logicalAndy)
// OR
let logicalOrX = false;
let logicalOrY = x ||= 10;
console.log(logicalOrY)
// Null Coalescing
let nullCoalescing;
nullCoalescing ??= 10;
console.log(nullCoalescing);

// Comparison
console.log("---Comparison Operator---");
let text1 = "A";
let text2 = "B";
let result = text1 < text2;
console.log(result);
result = text1 > text2;
console.log(result);
result = text1 <= text2;
console.log(result);
result = text1 >= text2;
console.log(result);
result = text1 != text2;
console.log(result);


// Conditionals
console.log("---Conditionals---");
// If else
let age = 50;
if (age > 12) {
  console.log("Teen");
}
else if (age > 18) {
  console.log("Young Adult");
}
else if (age > 35) {
  console.log("Middle Adult");
}
else {
  console.log("Late Adult");
}

// Switch

let day = 3;

switch (day) {
  case 1:
    console.log("Monday");
    break;

  case 2:
    console.log("Tuesday");
    break;

  case 3:
    console.log("Wednesday");
    break;

  case 4:
    console.log("Thursday");
    break;

  case 5:
    console.log("Friday");
    break;

  default:
    console.log("Invalid day");
}

// Ternary
let number = 7;
let numType = number % 2 === 0 ? "Even" : "Odd";
console.log(numType);


// Loops
console.log("---Loops---");
// For
for (let i = 1; i <= 5; i++) {
  console.log(i);
}
// While
let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
}
// Do... While
let j = 1;
do {
  console.log(j);
  j++;
} while (j <= 5);

// For In (Key/Property based)
let person = {
  name: "Het",
  age: 22,
  city: "Ahmedabad"
};

for (let key in person) {
  console.log(key, person[key]);
}

// For Of (Value based)
let fruits = ["Apple", "Banana", "Mango"];

for (let fruit of fruits) {
  console.log(fruit);
}

// Break
for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break;
  }
  console.log(i);
}
// Continue
for (let i = 1; i <= 5; i++) {
  if (i === 3) {
    continue;
  }
  console.log(i);
}