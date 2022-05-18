const data = require('./data.json');
console.log(data)


function addCard() {
    const front = document.getElementById("question-text")
    const back = document.getElementById("answer-text")
    const qSide = data["Questions"] = front
    const aSide = data['Answers'] = back
    
    console.log(qSide)
    console.log(aSide)
}

const addBtn = document.getElementById("question-text")
addBtn.addEventListener('click', () => {
    console.log("clicked")
})

$(document).ready(() => {

    function getRequest() {
        const buttonPressed = document.getElementById("deploy")
        buttonPressed.addEventListener('click', () => {
            console.log(buttonPressed)
        })
        return buttonPressed
    }
    
}) 


function getRequest() {
    const deployFunctions = document.getElementsByClassName("df")
    console.log(deployFunctions.childNodes)
    let ligma;
    ligma.addEventListener('click', () => {

    })
    buttonPressed.addEventListener('click', () => {
        console.log(buttonPressed)
    })
}

const dismiss = document.getElementsByClassName("btn-close");
dismiss.addEventListener('click', () => {
    const flashDiv = document.getElementsByClassName("alert")
    flashDiv.style.display = "none";
})