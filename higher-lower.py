import random

from flask import Flask

app = Flask(__name__)

target = random.randint(0, 9)
print(target)

@app.route('/')
def at_root():
    return "<h1 style='text-align:center'>Guess a number " \
           "between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:guess>/')
def guess_a_number(guess):
    if guess < target:
        return "<h1 style='color:red'>too low</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif guess > target:
        return "<h1 style='color:blue'>too high</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1 style='color:green'>correct</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)