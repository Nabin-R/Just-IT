// DOM - Document Object Model
console.log(document);

// DOM Query Methods - How to select elements from the dom in different ways

// getElementById() - allows you to select an element from the DOM via its ID
const heading = document.getElementById('heading');
console.log(heading);

// getElementsByClassName() - allows you to select elements by classname from the DOM
const liClass = document.getElementsByClassName('listItems');
console.log(liClass);

// getElementsByTagName() - allows you to select elements by their tagname from the DOM
const liElements = document.getElementsByTagName('li');
console.log(liElements);

// querySelector() - Allows you to pass a css selector to filter through elements
// querySelector will only select the first element that matches the selector
const paragraph = document.querySelector('p');
console.log(paragraph);

// querySelectorAll()
// querySelectorAll will select all elements that match
const paragraphs = document.querySelectorAll('p');
console.log(paragraphs);

// Style an element using the DOM
heading.style.backgroundColor = 'Orange';

// Styling multiple elements at once
for (let i = 0; i < paragraphs.length; i++) {
    paragraphs[i].style.backgroundColor = 'Violet';
}

// Creating elements via the DOM and adding them to the Document

// Creating a new list item requires the <ul> element to house the <li>

// Select the <ul> from the document and store it in a variable
const ul = document.querySelector('ul');
console.log(ul);

// Create a new <li> element using the createElement() method
const newListItem = document.createElement('li');
console.log(newListItem);

// Elements created with the DOM arent added to the document by default
// we need to add them to a specific part of the document manually
ul.append(newListItem);

// We can also modify the text content of an element with the innerText property
newListItem.innerText = 'Item 5';

// We can add a class to an element
newListItem.classList.add('listItems');

// We can also add an attribute to an element
newListItem.setAttribute('id', 'item5');

// Attributes can be removed
newListItem.removeAttribute('id');

// As can classes
newListItem.classList.remove('listItems');

// Elements can also be removed with the remove() method
newListItem.remove();





