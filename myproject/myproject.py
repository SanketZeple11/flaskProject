from flask import Flask

app = Flask(__name__)


@app.route("/")
def display():
    return "WELCOME TO THE SITE!!"


if __name__ == "__main__":
    app.run()
