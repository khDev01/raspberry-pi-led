var content = document.getElementById('content');
var rgbValue = document.getElementById('rgbColourValue');
var hexValue = document.getElementById('hexColourValue');
var answerMessage = document.getElementById('answer');
var buttons = document.getElementsByClassName('colourButton');
buttons[0]

function setButtonColour(button, red, green, blue){
    button.setAttribute(
    'style',
    'background-color: rgb('+ red +','+ green +','+ blue +');'
    );
}

function makeColourValue(){
    return Math.round(Math.random()*255);
}

function componentToHex(c) {
	var hex = c.toString(16);
	return hex.length == 1 ? "0" + hex : hex;
}

function rgbToHex(r, g, b) {
	return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
}

function startGame() {
	
	answerMessage.innerHTML = "";

  var answerButton = Math.round(Math.random() * (buttons.length - 1));

  for (var i = 0; i < buttons.length; i++) {

    var red = makeColourValue();
    var green = makeColourValue();
    var blue = makeColourValue();

    setButtonColour(buttons[i], red, green, blue);

    if (i === answerButton) {
      rgbValue.innerHTML = `RGB(${red}, ${green}, ${blue})`;


			hexValue.innerHTML = `HEX: `+(rgbToHex(red, green, blue));
    }

    buttons[i].addEventListener('click', function(){
        if (this === buttons[answerButton]) {
            answerMessage.innerHTML = "Correct!";
        } else {
            answerMessage.innerHTML = "Wrong answer! Guess again!";
        }
    });

  }

}

document.getElementById('resetButton').addEventListener('click', startGame);

startGame();



