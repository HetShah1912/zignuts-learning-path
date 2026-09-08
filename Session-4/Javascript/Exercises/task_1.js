// Task 1: Need to create JavaScript functions for a sum of numbers in the string (Example
// like “foo8bar8cat2tc2”)

let sumOfNumbers = (str) => {
  /// Suppose String : abc123def456
  // RegEx :: \d : digits, + : 123 and 456 together not 1,2,3,4,5,6 and g : global(find all occurence)
  const numbers = str.match(/\d+/g);
  // console.log(numbers)
  let sum = numbers.reduce((acc, number) => {
    acc += Number(number);
    return acc;
  }, 0);
  return sum;
}

console.log("Sum : " + sumOfNumbers("foo8bar8cat2tc2"));