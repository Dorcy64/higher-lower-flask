from flask import Flask
from random import randint

RANDOM_NUMBER = randint(0, 9)

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Guess a number  between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='500'>"


@app.route("/<int:number>")
def guessed_number(number):
    global RANDOM_NUMBER
    if RANDOM_NUMBER == number:
        RANDOM_NUMBER = randint(0, 9)
        return f"<h1 style='color: green;'>{number} is correct</h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='500'>"
    elif number > RANDOM_NUMBER:
        return f"<h1 style='color: purple;'>{number} is too high</h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width=500>"
    elif number < RANDOM_NUMBER:
        return f"<h1 style='color: red;'>{number} is too Low</h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='500'>"


if __name__ == "__main__":
    app.run(debug=True)
