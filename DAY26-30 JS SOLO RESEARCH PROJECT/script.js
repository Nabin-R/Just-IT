// API, DOM, Interractive website.
// async function getChar(para1) {
//     let apiURL = `https://genshin.jmp.blue/characters/${para1}`;
//     const response = await fetch(apiURL);
//     const apiData = await response.json()
//     return apiData;
// }
// async function getCard(para1) {
//     let apiURL = `https://genshin.jmp.blue/characters/${para1}/card`;
//     const response = await fetch(apiURL);
//     const apiData = await response.url
//     return apiData;
// }

async function getAll(para1) {
    let apiURL = `https://genshin.jmp.blue/characters/${para1}`;
    let apicardURL = `https://genshin.jmp.blue/characters/${para1}/card`;
    const response = await fetch(apiURL);
    const apiData = await response.json();
    console.log(para1)
    if (para1 == 'chevreuse' || para1 == 'navia') {

        var returndata = [apiData, 'https://seeklogo.com/images/G/genshin-japan-logo-7BBE5D9029-seeklogo.com.png'];
    }
    else {
        const responseC =  await fetch(apicardURL);
        const apiDataC =  responseC.url;

        var returndata = [apiData, apiDataC]
    }

    return returndata;
}

async function getData() {
    let apiURL = `https://genshin.jmp.blue/characters/`;
    const response = await fetch(apiURL);
    const apiData = await response.json()
    //console.log(apiData);
    return apiData;
}

const nestedobject = {};

const ImageHolder = {};


const list = document.getElementsByClassName(`list`);
document.addEventListener(`DOMContentLoaded`, async () => {    
let apiData = [];
    try {
        apiData = await getData();
    for (i = 0; i < apiData.length; i++) {
        // let infoChar = await getChar(apiData[i])
        // let infoCard = await getCard(apiData[i])
        // nestedobject[apiData[i]] = infoChar
        // ImageHolder[apiData[i]] = infoCard

        let infoChar = await getAll(apiData[i])
        nestedobject[apiData[i]] = infoChar[0]
        ImageHolder[apiData[i]] = infoChar[1]
        
    }
    }
    catch (error){
        console.log(error);
    }

    document.getElementById(`removabletext`).remove()
    console.log(nestedobject);
    console.log(ImageHolder);

    for (i = 0; i < apiData.length; i++) { 
        let newTile = document.createElement(`button`);
        newTile.setAttribute(`onClick`, "InfoClick('"+apiData[i]+"')");
        newTile.setAttribute(`class`, nestedobject[apiData[i]].gender + " CharButton " + nestedobject[apiData[i]].vision);
        //console.log(nestedobject[apiData[i]]);
        newTile.innerHTML = nestedobject[apiData[i]].name
        list[0].append(newTile)
    }
    
    console.log('loaded')

})

function FilterClick(f) {
    buttons = document.getElementsByClassName(`CharButton`);
    pyro = document.getElementsByClassName(`Pyro`);
    geo = document.getElementsByClassName(`Geo`);
    hydro = document.getElementsByClassName(`Hydro`);
    cryo = document.getElementsByClassName(`Cryo`);
    electro = document.getElementsByClassName(`Electro`);
    anemo = document.getElementsByClassName(`Anemo`);
    dendro = document.getElementsByClassName(`Dendro`);
    male = document.getElementsByClassName(`Male`);
    female = document.getElementsByClassName(`Female`);

    for (i =0; i < buttons.length; i++) {
        buttons[i].style.display = "none";
    }

    if ( f == `default`){
        for (i =0; i < buttons.length; i++) {
           buttons[i].style.display = "block";
      }
    }

    else if (f == `pyro`) {
        for (i =0; i < pyro.length; i++) {
        pyro[i].style.display = "block";
    }
    }
    else if (f == `geo`) {
            for (i =0; i < geo.length; i++) {
            geo[i].style.display = "block";
        }
    }
    else if (f == `hydro`) {
            for (i =0; i < hydro.length; i++) {
            hydro[i].style.display = "block";
        }
    }
    else if (f == `cryo`) {
            for (i =0; i < cryo.length; i++) {
            cryo[i].style.display = "block";
        }
    }
    else if (f == `electro`) {
            for (i =0; i < electro.length; i++) {
            electro[i].style.display = "block";
        }
    }
    else if (f == `dendro`) {
            for (i =0; i < dendro.length; i++) {
            dendro[i].style.display = "block";
        }
    }
    else if (f == `anemo`) {
            for (i =0; i < anemo.length; i++) {
            anemo[i].style.display = "block";
        }
    }
    else if (f == `male`) {
            for (i =0; i < male.length; i++) {
            male[i].style.display = "block";
        }
    }
    else if (f == `female`) {
            for (i =0; i < female.length; i++) {
            female[i].style.display = "block";
        }
    }
}

function InfoClick(id) {
    let currentChar = nestedobject[id]
    let name = document.getElementById(`previewName`)
    let title = document.getElementById(`previewTitle`)
    let rarity = document.getElementById(`previewRarity`)
    let nation = document.getElementById(`previewNation`)
    let sex = document.getElementById(`previewSex`)
    let element = document.getElementById(`previewElement`)
    let desc = document.getElementById(`previewDesc`)

    name.innerText = "Name: " + currentChar.name
    title.innerHTML = "Title: " + currentChar.title
    rarity.innerText = "Rarity: " + currentChar.rarity + " Star"
    nation.innerHTML = "Nation: " + currentChar.nation
    sex.innerText = "Sex: " + currentChar.gender
    element.innerHTML = "Element: " + currentChar.vision
    desc.innerText = "Description: " + currentChar.description

    document.getElementById(`ImageView`).src = ImageHolder[id]

}