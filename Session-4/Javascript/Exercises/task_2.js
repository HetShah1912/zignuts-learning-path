// Task 2: Need to create a JavaScript function for the sum of a string (Example like "1.5,
// 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9")

let sumOfString = (str) => {
  let numbers = str.split(",");
  // console.log(numbers);
  let sum = numbers.reduce((acc, number) => {
    acc += Number(number);
    return acc;
  }, 0);
  return sum;
}

console.log("Sum : "+sumOfString("1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"));