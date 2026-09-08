// Task 6: Write a program to find the factorial of a number using a recursive function

function factorial(num) {
  if (num < 0) {
    return -1;
  }
  else if (num === 1 || num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(7))