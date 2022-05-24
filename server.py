from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return "<h1>Hello, Flask!</h1>" \
           "<p>paragraph</p>"

def make_bold(func):
    def wrapper_function():
        return f'<b>{func()}</b>'
    return wrapper_function

def make_emphasis(func):
    def wrapper_function():
        return f'<em>{func()}</em>'
    return wrapper_function

def make_underline(func):
    def wrapper_function():
        return f'<u>{func()}</u>'
    return wrapper_function

@app.route('/test')
@make_bold
@make_emphasis
@make_underline
def decorator_test():
    return '<h1 style="text-align: center">test<h1>'

@app.route('/<name>/<int:number>')
def bye_flask(name, number):
    return f"hello, there {name}, you are {number} years old"


if __name__ == '__main__':
    app.run(debug=True)
