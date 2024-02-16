
// function loop() {
//     var age = prompt("How old are you?");
//     if (age > 17) {
//         alert("Welcome");
//     }

//     else if (age < 18) {
//         alert("You unable to access the website due to age")
//     }
//     else {
//         loop()
//     }
// }

// loop();


// var mark = 90;

// switch (mark) {
//     case 100:
//         text = "100/100";
//         break;
//     case 90:
//         text = "90/100";
//         break;
//     case 80:
//         text = "80/100";
//         break;
//     case 70:
//         text = "70/100";
//         break;
//     case 60:
//         text = "60/100";
//         break;
//     case 50:
//         text = "50/100";
//         break;
//     case 40:
//         text = "40/100";
//         break;
//     case 30:
//         text = "30/100";
//         break;
//     case 20:
//         text = "20/100";
//         break;
//     case 10:
//         text = "10/100";
//         break;
//     case 0:
//         text = "0/100";
//         break;
//     default:
//         text = "Broken";
// }

// alert(text);

// var markten = 39;

// if (markten >= 70 && markten < 100) {
//     output = "Distinction"
// }
// else if (markten < 70 && markten > 40) {
//     output = "Pass"
// }
// else {
//     output = "Fail"
// }

// alert(output);


function loop() {
    var password = prompt("Type in Password:")
    if (password.length >= 8) {
        alert("Password has been accepted");
    }
    else {
        alert("Your password is too short, please re-enter a new password:")
        loop()
    }
    var check = password.length >= 8 ? "Password is Over 8 Letters" : "Password is under 8 Letters";
    console.log(check);
}

loop();

var numberdivision = 15;

if (numberdivision % 5 == 0 && numberdivision % 3 == 0) {
    console.log("Fizz Buzz");
}
else if (numberdivision % 5 == 0) {
    console.log("Buzz");
}
else if (numberdivision % 3 == 0) {
    console.log("Fizz");
}
else {
    console.log("Unable to divide by 3 or 5");
}