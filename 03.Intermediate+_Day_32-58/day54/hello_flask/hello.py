from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

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