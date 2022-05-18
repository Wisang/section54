from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return "Hello, Flask!"


@app.route('/<name>/<age>')
def bye_flask(name, age):
    return f"hello, there {name}, you are {age} years old"


if __name__ == '__main__':
    app.run(debug=True)
