const question = document.getElementById("question");
const choices = Array.from(document.getElementsByClassName("choice-text"));
const progressText = document.getElementById("progressText");
const scoreText = document.getElementById("score");
const progressBarFull = document.getElementById("progressBarFull");
let currentQuestion = {};
let acceptingAnswers = false;
let score = 0;
let questionCounter = 0;
let availableQuesions = [];

let questions = [
];
const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 10;
var difficulty = 0;

startGame = () => {
  questionCounter = 0;
  score = 0;
  availableQuesions = [...questions];
  getNewQuestion();
};

function UserAction(data) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
        geneareted_question = this.responseText;
        geneareted_question = JSON.parse(geneareted_question)
        console.log(currentQuestion);
        question.innerText = geneareted_question.question;
        if(geneareted_question.answer == "yes"){
          geneareted_question.answer = 1;
        }
        else{
          geneareted_question.answer = 2;
        }
       }
  };
  xhttp.open("POST", "http://127.0.0.1:5000/getquestion", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  xhttp.send(data);
}



getNewQuestion = () => {
  if (questionCounter >= MAX_QUESTIONS) {
    username = sessionStorage.getItem("username")
    difficulty_level = difficulty/MAX_QUESTIONS;
    var enddata = JSON.stringify({"username" : username.toString(),"marks" : scoreText.innerText.toString(), "difficulty":difficulty_level.toString()})
    var xhttp1 = new XMLHttpRequest();
    xhttp1.open("POST", "http://127.0.0.1:5000/test_details", true);
    xhttp1.setRequestHeader("Content-type", "application/json");
    xhttp1.send(enddata);
    alert("Your Responses have been taken please find the result in the results section");
    return window.location.assign("end.html"); 
    }
  questionCounter++;
  progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;
  progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`;
  if(questionCounter == 1){
    questionIndex = Math.floor((Math.random()*(9-1)) + 1);
  }
  else{
    if(classToApply === "correct"){
      questionIndex++;
      if(questionIndex == 10){
        questionIndex = Math.floor((Math.random()*(9-7)) + 7);
      }
    }
    else{
      questionIndex--;
      if(questionIndex == 0){
        questionIndex = Math.floor((Math.random()*(2-1)) + 1);
      }
    }
  }
  difficulty += questionIndex;
  console.log(questionIndex)
  var data = JSON.stringify({"class_q" : questionIndex.toString()})
  UserAction(data);
  availableQuesions.splice(questionIndex, 1);
  acceptingAnswers = true;
};

choices.forEach(choice => {
  choice.addEventListener("click", e => {
    if (!acceptingAnswers) return;
    acceptingAnswers = false;
    const selectedChoice = e.target;
    const selectedAnswer = selectedChoice.dataset["number"];
    classToApply =
      selectedAnswer == geneareted_question.answer ? "correct" : "incorrect";

    if (classToApply === "correct") {
      incrementScore(CORRECT_BONUS);
    }

    selectedChoice.parentElement.classList.add(classToApply);

    setTimeout(() => {
      selectedChoice.parentElement.classList.remove(classToApply);
      getNewQuestion();
    }, 1000);
  });
});

incrementScore = num => {
  score += num;
  scoreText.innerText = score;
};

startGame();
