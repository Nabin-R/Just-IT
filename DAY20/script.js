/*
function numbering(n1, n2, type) {
    if (type == `add`) {
        console.log(n1 + n2)
        console.log("ADD")
    }
    else if (type == `subtract`) {
        console.log(n1 - n2)
        console.log("SUBTRACT")
    }
    else if (type == `multiply`) {
        console.log(n1 * n2)
        console.log("MULTIPLY")
    }
    else if (type == `divide`) {
        console.log(n1 / n2)
        console.log("DIVIDE")
    }
    else {
        alert(`Wrong input`);
    }
}

function Kalert(inp) {
    alert(inp);
}

var IInput = prompt("Do you want to add, subtract, multiply or divide 5 and 10");
var Dinput = prompt("Say something");


var num1 = 5;
var num2 = 10;
Kalert(Dinput);
numbering(num1, num2, IInput);
console.log(IInput)
*/
/*
1: Write a function that takes in a first name and a surname as arguments and returns a message greeting them.
2: Write a function that takes in a string as an argument and sorts the string into alphabetical order and returns the result.
3: Write a cash machine / atm function that takes in a withdrawal amount and a pin
 number as an argument and compares the pin and withdrawal amount against a stored 
 pin and account balance. If the pin matches and the balance is sufficient approve 
 the transaction, if not decline the transaction.
4: Write a function that calls another function to calculate the gross pay of items purchase, this function will take 2 arguments for quantity and cost. Once gross has been calculated apply VAT and return the value.
*/

// Task 1

let firstName = `Walter`;
let surName = `White`;

function greet(f, s) {
    alert(`Hello ${f} ${s}`)
}

greet(firstName, surName);
// Task 2

let text = `Rearrange this word to the alphabet`

function rearrange(s) {
    return s.toLowerCase().split("").sort().join("");
}

console.log(rearrange(text));

//Task 3


function atmMachine(withdrawal, pin) {
    if (withdrawal <= 250 && pin == 1337) {
        console.log(`Your withdrawal transaction has been complete`)
    }
    else if (pin == 1337) {
        console.log(`You cannot withdraw more than £250`)
    }
    else {
        console.log(`Pin is incorrect`)
    }
}

atmMachine(500, 1337);
atmMachine(200, 1337);
atmMachine(200, 1338);