/*
Create a new index.html and script.js in order to complete the following tasks:
1: Add a <h1> element to the HTML with some text inside it. 
For this step HTML can be used, however the remaining steps must be completed 
using JavaScript and the DOM.
*/

/*
2: Using a DOM query method I would like you to select the h1 element from the 
DOM and store it in your JavaScript file in a variable.
*/
const headerquery = document.querySelector(`h1`);
/*
3: Add an ID, update the text content and styling of your <h1> element 
using the DOM.
*/
headerquery.setAttribute(`id`, `Header`);
headerquery.setAttribute
headerquery.innerText = `Webpage Header`;
headerquery.style.backgroundColor = "Cyan";
/*
4: Using the DOM I would like you to create a <ul> element and 3 <li>’s and
add them to the document.
*/

//5: Edit the text content of each <li> and change the colour of the <li>’s.

const newTable = document.createElement(`ul`);
newTable.setAttribute('id', 'Table');
newTable.innerText = `Table`;
newTable.style.marginLeft = `30px`;
newTable.style.marginTop = `20px`;
document.body.append(newTable);

for (let i = 0; i < 3; i++) {
    const newChild = document.createElement(`li`);
    newTable.append(newChild)
    newChild.innerText = `List ${i + 1}`;
    newChild.style.color = `rgb(${Math.floor(Math.random() * 255) + 1}, ${Math.floor(Math.random() * 255) + 1}, ${Math.floor(Math.random() * 255) + 1})`
}


//6: Finally remove your h1 element from the document.

document.getElementById(`Header`).remove();
