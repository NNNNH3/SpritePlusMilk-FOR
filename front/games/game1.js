const question = document.getElementById('question');
const input = document.getElementById('input');
const result = document.getElementById('result');
let health = document.getElementById("health");

let num1 = Math.floor(Math.random() * 10) + 1;
let num2 = Math.floor(Math.random() * 10) + 1;
question.innerText = `${num1} x ${num2} = ?`;

function game(){
    correctAnswer = num1 * num2;
    if (parseInt(input.value) == correctAnswer) {
    health.value =health.value-10 ;
    console.log(health.value) 
    result.innerText = "Ура, -HP";
  } else {
    result.innerText = "Ответ неправильный";
  }
    num1 = Math.floor(Math.random() * 10) + 1;
    num2 = Math.floor(Math.random() * 10) + 1;
    question.innerText = `${num1} x ${num2} = ?`;
    if(health.value==0){
        window.location.href = 'http://127.0.0.1:5500/hack2023uunt/index.html';
    }
}
