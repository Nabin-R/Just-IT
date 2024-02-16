
// prompt are always string inputs.
// let value = prompt("enter value")
// console.log(typeof value)

// Convert numbers

let c = `10`
console.log(Number(c) + 10);
console.log(Number(`text`)); //Console: NaN

// Commas do not convert to numbers when working with decimals
// Boolean. True = 1, False = 0


//  Task

let x = true;
let y = 10;
let z = `30`

console.clear();

console.log(Number(x), typeof x);
console.log(Number(y), typeof y);
console.log(Number(z), typeof z);
console.log(String(x), typeof x);
console.log(String(y), typeof y);
console.log(String(z), typeof z);

console.log('12' / 2);
console.log(2 * '2');
console.log('10' / 2);
console.log('10' % 2);
console.log(true * 7);

console.clear();

console.log('1' + 2);
console.log('1' + 2 + true);
console.log('12' + undefined);
console.log('12' + null);
console.log(2 + '1');
console.log(2 + true);

console.log(3 + 4 + true + '2' + 10 + true + 11 + '2' + 1);

console.log(Math.floor(Math.random() * 5) + 1);

const userName = prompt("Enter Name:");
console.log(`Hello, ${userName}!`);

const userNumber = prompt("Enter Number:");
const result = userNumber * 10;
alert(`10X your number: ${result}`);