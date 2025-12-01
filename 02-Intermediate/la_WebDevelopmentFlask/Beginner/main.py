from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper


def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper


@app.route("/")
def hello_world():
    return "<h1 style='color:blue; text-align:center'>Hello, World!</h1>" \
           "<p>This is my first Flask app.</p>" \
           "<img src='https://media.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif' alt='funny gif'>"


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye() -> str:
    return "Bye"


@app.route("/username/<name>/<int:number>")
def greet(name: str, number: int) -> str:
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)  # Reloads server on code change
