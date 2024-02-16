const dataOutput = document.getElementById(`dataOutput`);

async function getData() {
    let apiURL = `https://api.adviceslip.com/advice`;
    const response = await fetch(apiURL);
    const apiData = await response.json()
    return apiData;
}

document.addEventListener(`DOMContentLoaded`, async () => {
    let apiData = [];
    try {
        apiData = await getData();
        dataOutput.innerText = apiData.slip.advice;
    }
    catch (error){
        console.log(error);
    }

})