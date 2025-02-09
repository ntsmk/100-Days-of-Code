from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
@make_underline # it needs to be under @app.route("/") to work
@make_bold
@make_emphasis
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>this is a paragraph</p>"
            "<img src='https://media.giphy.com/media/l0ExdMHUDKteztyfe/giphy.gif?cid=790b7611hxqze999001pbvqcopj7za9q432ajwpsusayqq8k&ep=v1_gifs_search&rid=giphy.gif&ct=g' alt='GIF'>")

@app.route("/about")
def about():
    return "<p>This is the about page.</p>"

@app.route("/bye")
def bye():
    return "<p>Goodbye!</p>"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello, {name + '12'}! How are you?? I am good. You are {number} years old</p>"

if __name__ == "__main__":
    app.run(debug=True) # debug=True will automatically restart the server when changes are made to the code.