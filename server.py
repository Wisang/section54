import unittest
from flask import Flask

app = Flask(__name__)


class BackendTest(unittest.TestCase):
    @app.route('/')
    def hello_flask():
        print("function: " + __name__)
        return "Hello, Flask!"

    def test_run(self):
        app.run()


if __name__ == '__main__':
    unittest.main()


# @app.route('/')
# def hello_flask():
#     print("function: " + __name__)
#     return "Hello, Flask!"

# if __name__ == '__main__':
#     app.run()
