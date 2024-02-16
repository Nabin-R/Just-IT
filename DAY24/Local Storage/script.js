// Access all our relevant elements from the DOM
const keyInput = document.getElementById("keyInput");
const valueInput = document.getElementById("valueInput");
const submitBtn = document.getElementById("submitBtn");

const saveToLocalStorage = () => {
    // Store the input value in variables of key and value
    let key = keyInput.value;
    let value = valueInput.value;
    // Check that we have a key and a value, if so call setItem(key,value)
    if (key && value) {
        localStorage.setItem(key, value);
    }
}

submitBtn.addEventListener("click", saveToLocalStorage);

console.log(localStorage);
