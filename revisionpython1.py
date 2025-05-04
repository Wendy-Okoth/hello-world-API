from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<div style="text-align: center; background-color: white;"><p style="color: red; text-decoration: underline; font-weight: bold;">Hello, World!</p></div>'


if __name__ == '__main__':
    app.run(debug=True)
