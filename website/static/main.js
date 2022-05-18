//DATA
var authToken = null;



function retrieveQuestions() {
  // if (authToken == null) return;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      let data = JSON.parse(this.response)['items']
      console.log(data)
      document.getElementById("test").innerHTML = data;
    }
  }
  xhttp.open("GET", "/api/questions", true)
  xhttp.send()
}
retrieveQuestions()

// add questions
function addQuestion() {
  // if (authToken == null) return;
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      let data = JSON.parse(this.response)['items']
      console.log(data)
      document.getElementById("test").innerHTML = data;
    }
  }

  xhttp.open("POST", "/api/questions", true)
  xhttp.send()
}
retrieveQuestions()




// Randomises the answers to A B C or D
function assignAnswer(options) {

  const letters = ["A","B","C","D"];
  let answersList = [];
  let answerLetters = [];
  let count = 0
  for (i=0;answersList.length < 4;i++) {
    let letter = letters[Math.floor(Math.random()*letters.length)];
    if (answerLetters.includes(letter) == false) {
      answerLetters.push(letter);
      answersList.push([letter, options[count]])
      count ++;
    }
  }
  return answersList;
}

//fetch todays game data from server
function getGameData() {

  data = new Object()

  // retrieve dict from backend
  data.gameData = [{
    "id": 1,
    "question": "Where is the heart rate slowed?",
    "answer": "AV Node",
    "alt_answers": [
      "SA Node",
      "Perkinje Fibres",
      "right atria"
    ]
  },
  {
    "id": 2,
    "question": "Which of the following decreases heart rate?",
    "answer": "Acetylcholine",
    "alt_answers": [
      "Adrenaline",
      "Noradrenaline",
      "Dopamine"
    ]
  },
  {
    "id": 3,
    "question": "Where is the fusiform face area?",
    "answer": "Fusiform gyrus",
    "alt_answers": [
      "Occipital lobe",
      "Frontal lobe",
      "Parietal lobe"
    ]
  },
  {
    "id": 4,
    "question": "Where is the occulomotor nuclei located?",
    "answer": "Midbrain",
    "alt_answers": [
      "Pons",
      "The eye",
      "Medulla oblongata"
    ]
  },
  {
    "id": 5,
    "question": "What is the first neuron in the visual pathway",
    "answer": "Retinal ganglion cells",
    "alt_answers": [
      "Perkinje Fibres",
      "Photoreceptors",
      "Dentate nucleus"
    ]
  },
  {
    "id": 6,
    "question": "Whats 9 + 10",
    "answer": "21",
    "alt_answers": [
      "19",
      "90",
      "1"
    ]
  },
  {
    "id": 7,
    "question": "Who is cracked at fortnight my guy",
    "answer": "Jam Fold",
    "alt_answers": [
      "Jel betty",
      "Booper Brown",
      "Jaqueline Sturg"
    ]
  }]

  // combine answers and alt_answers into one list for all question data
  data.sortQuestionList = () => {
    let questionListSorted = []
    let count = 0
    for (i=0; questionListSorted.length < data.gameData.length; i++) {
      let questionList = []
      questionList.push(data.gameData[count]["answer"])
      for (j=0;questionList.length < 4; j++) {
        questionList.push(data.gameData[count]["alt_answers"][j])
      }
      questionList = assignAnswer(questionList)
      questionListSorted.push(questionList)
      count ++
    }
    return questionListSorted
  }
  return data
}

// Sorted answer list
let finalAnswerList = getGameData().sortQuestionList()

// Render question and answers
function startQuizzle() {

  // Get question number and game data
  let questionCount = score.length
  const currentGameData = getGameData().gameData

  // Render question 
  const question = document.getElementById('question')
  question.innerHTML = currentGameData[questionCount]["question"]

  // Render answers
  const options = document.getElementById('options').getElementsByTagName("p")
  for (i=0; i < options.length; i++) {
    if (finalAnswerList[questionCount][i][0] == 'A') {
      options[0].innerHTML = finalAnswerList[questionCount][i][1]
    } else if (finalAnswerList[questionCount][i][0] == 'B') {
      options[1].innerHTML = finalAnswerList[questionCount][i][1]
    } else if (finalAnswerList[questionCount][i][0] == 'C') {
      options[2].innerHTML = finalAnswerList[questionCount][i][1]
    } else if (finalAnswerList[questionCount][i][0] == 'D') {
      options[3].innerHTML = finalAnswerList[questionCount][i][1]
    }
  }
  
}

// score variable keeps track of question count too (score.length)
let score = []
// Load first question and answers
startQuizzle()

// checks if answer is correct and updates score
function submitAnswer(answer) {
  let questionCount = score.length
  const currentGameData = getGameData().gameData
  if (questionCount != 7){
    const correctAnswer = currentGameData[questionCount]["answer"]
    for (i=0;i < finalAnswerList[questionCount].length;i++) {
      if (finalAnswerList[questionCount][i].includes(correctAnswer)) {
        if (answer == finalAnswerList[questionCount][i][0]) {
          score.push(1)
          console.log("correct")
        } else {
          score.push(0)
          console.log("incorrect")
        }
        getScore(score)
        if (score.length == 7) {
          // add winning message
          alert("congrats")
        }
      }
    }
  } else {
      console.log("Final Score: " + score)
      getScore(score)
  }
  startQuizzle()
  return score
}

// Convert score to University grades and update styling
function getScore(answerList) {
  const scoreTag = document.getElementById("score");
  const scoreBlocks = document.getElementById("score-blocks");
  const gradeTag = document.getElementById("grade");
  let score = 0;
  for (i = 0; i < answerList.length; i++) {
    if (answerList[i] == 1) {
      score++;
      scoreBlocks.children[i].style.backgroundColor = "green"
    } else {
      scoreBlocks.children[i].style.backgroundColor = "red"
    }
  }
  let grade = Math.round((score / answerList.length) * 100)
  scoreTag.innerHTML = `${grade} %`
  //console.log(score)

  if (grade >= 80) {
    scoreTag.style.color = "green"
    gradeTag.innerHTML = "High Distinction"
  } else if (grade < 80 && grade >= 70) {
    scoreTag.style.color = "#90EE90"
    gradeTag.innerHTML = "Distinction"
  } else if (grade < 70 && grade >= 60) {
    scoreTag.style.color = "yellow"
    gradeTag.innerHTML = "Credit"
  } else if (grade < 60 && grade >= 50) {
    scoreTag.style.color = "orange"
    gradeTag.innerHTML = "Pass"
  } else if (grade < 50) {
    scoreTag.style.color = "red"
    gradeTag.innerHTML = "Fail"
  }
}
getScore(score)

// dark vs light mode
function modeSwitch() {
  const switchButton = document.getElementById("appearance-switch");
  switchButton.addEventListener('click', () => {
    console.log("yes")
  });
}

function like(postId) {
  const likeCount = document.getElementById(`likes-count-${postId}`);
  const likeButton = document.getElementById(`like-button-${postId}`);

  fetch(`/like-post/${postId}`, { method: "POST" })
    .then((res) => res.json())
    .then((data) => {
      likeCount.innerHTML = data["likes"];
      if (data["liked"] === true) {
        likeButton.className = "fas fa-thumbs-up";
      } else {
        likeButton.className = "far fa-thumbs-up";
      }
    })
    .catch((e) => alert("Could not like post."));
}

/* Referenced Components */

/* Dropdown from w3 schools https://www.w3schools.com/howto/howto_js_dropdown.asp */
function dropdownFunc(a) {
  a.parentNode.getElementsByClassName("dropdown-content")[0].classList.toggle("show");
  }
  
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }

  var coll = document.getElementsByClassName("collapsible");
  var i;
  
  for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
      this.classList.toggle("active");
      var content = this.nextElementSibling;
      if (content.style.display === "block") {
        content.style.display = "none";
      } else {
        content.style.display = "block";
      }
    });
  }

