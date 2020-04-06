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
  {
    question: "Inside which HTML element do we put the JavaScript??",
    choice1: "<script>",
    choice2: "<javascript>",
    choice3: "<js>",
    choice4: "<scripting>",
    answer: 1
  },
  {
    question:
      "What is the correct syntax for referring to an external script called 'xxx.js'?",
    choice1: "<script href='xxx.js'>",
    choice2: "<script name='xxx.js'>",
    choice3: "<script src='xxx.js'>",
    choice4: "<script file='xxx.js'>",
    answer: 3
  },
  {
    question: " How do you write 'Hello World' in an alert box?",
    choice1: "msgBox('Hello World');",
    choice2: "alertBox('Hello World');",
    choice3: "msg('Hello World');",
    choice4: "alert('Hello World');",
    answer: 4
  }
];

//CONSTANTS
const CORRECT_BONUS = 10;
const MAX_QUESTIONS = 10;

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
    //go to the end page
    return window.location.assign("/end.html");
  }
  questionCounter++;
  progressText.innerText = `Question ${questionCounter}/${MAX_QUESTIONS}`;
  //Update the progress bar
  progressBarFull.style.width = `${(questionCounter / MAX_QUESTIONS) * 100}%`;
  // alert(questionCounter);
  if(questionCounter == 1){
    questionIndex = Math.floor((Math.random()*(9-1)) + 1);
    // alert(questionIndex)
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
