let nums = [84, 34, 11, 465, 79, 34, 78];
for (let i = 0; i < nums.length; i++) {

    if (nums[i] % 2 == 0) {
        console.log(nums[i])
    }
}
// Tasks:
// 1: Create an array of your favourite films / TV shows, up to 5 items. Use an array method to add 2 more items to your array. Use a loop to cycle through the array and log each item to the console.
// 2: Generate 10 random numbers between 1-100 and log them to the console.
// 3: Create a loop that counts backwards from 20-0.
// 4: Generate 5 random numbers between 1-50. For each number generated, check if 
// the number is divisible by 5 or not. Log whether it is divisible or not to 
// the console.

// Task 1
console.log(`Task 1`)
let film = [`Film 1`, `Film 2`, `Film 3`, `Film 4`, `Film 5`]

for (let c = 0; c < 2; c++) {
    film.push(`Film ` + (c + 6))
}
for (let i = 0; i < film.length; i++) {
    console.log(film[i])
}

// Task 2
console.log(`Task 2`)
let randomnumber = [];
for (let rm = 0; rm < 10; rm++) {
    randomnumber.push(Math.floor(Math.random() * 100) + 1);
}
console.log(randomnumber);

// Task 3
console.log(`Task 3`)

for (let lp = 20; lp > 0; lp--) {
    console.log(lp);
}

// Task 4
console.log(`Task 4`)

let t5 = [];

for (let x = 0; x < 5; x++) {
    t5.push(Math.floor(Math.random() * 50) + 1);
    console.log(t5[x]);
    if (t5[x] % 5 == 0) {
        console.log(`is Dividable by 5`);
    }
}

// Task 5

let nums2 = [84, 34, 11, 465, 79, 34, 78];
let lastnumber = nums2[0];

for (let q = 0; q < nums2.length; q++) {
    if (nums2[q] > lastnumber) {
        lastnumber = nums2[q]
    }

}

console.log(lastnumber);