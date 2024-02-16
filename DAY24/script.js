// Access all our relevant elements from the DOM
const keyInput = document.getElementById("keyInput");
const valueInput = document.getElementById("valueInput");
const submitBtn = document.getElementById("submitBtn");


function saveToLocalStorage() {
    // Store the input value in variables of key and value
    let key = keyInput.value;
    let value = valueInput.value;
    // Check that we have a key and a value, if so call setItem(key,value)
    if (key && value) {
        localStorage.setItem(key, value);
    }
    console.log(localStorage);
}


const clearbutton = document.getElementById("ClearData");

const clearLocalStorage = () => {
    localStorage.clear();
    console.log(localStorage);
}

const searchInput = document.getElementById(`searchInputData`)
const searchButton = document.getElementById(`searchButton`)
const outputValue = document.getElementById(`outputvalue`)


function search() {
    var item = localStorage.getItem(searchInput.value);
    if (item != null) {
        outputValue.innerHTML = `Key: ${searchInput.value}, Value: ${item}`
    }
    else {
        outputValue.innerHTML = `local storage item doesn't exist`
    }
    searchInput.value = ``
};

submitBtn.addEventListener("click", saveToLocalStorage);
clearbutton.addEventListener("click", clearLocalStorage);
searchButton.addEventListener(`click`, search);
console.log(localStorage);