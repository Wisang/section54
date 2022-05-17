import unittest
import requests
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_flask():
    return "Hello, Flask!"


print(__name__)

if __name__ == '__main__':
    app.run()
