/*
const heading = document.getElementById('heading');

heading.addEventListener('click', () => {
    console.log(`The h1 element has been clicked`)
})

let greeting = () => {
    console.log(`Hello`)
}


heading.addEventListener('click', greeting)

let string = ``;
window.addEventListener(`keypress`, (e) => {
    string += e.key;
    console.log(string);
}) */


// TASK 1
const imageButton = document.getElementById('HideImage');
const image = document.getElementById('Image');

let imagevisible = true;

imageButton.addEventListener('click', () => {
    image.style.visibility == `hidden` ? image.style.visibility = 'visible' : image.style.visibility = 'hidden'
})

//TASK 2

const inputfield = document.getElementById(`inputfield`);
const submitbutton = document.getElementById(`submit`);
var outputsec = document.getElementsByClassName(`tiles`);

submitbutton.addEventListener(`click`, () => {
    const newTile = document.createElement(`p`);
    newTile.innerText = inputfield.value;
    outputsec[0].prepend(newTile);
    inputfield.value = ``;
})

// TASK 3
const leftbutton = document.getElementById('countleft');
const rightbutton = document.getElementById('countright');
const counter = document.getElementById('countertext')

let counttrack = 0;

function update() {
    counter.innerText = counttrack
}
rightbutton.addEventListener(`click`, () => {
    counttrack += 1;
    update();
})
leftbutton.addEventListener(`click`, () => {
    counttrack -= 1;
    update();
})