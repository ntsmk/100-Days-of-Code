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

@app.route("/username/<name>")
def greet(name):
    return f"<p>Hello, {name}!</p>"

if __name__ == "__main__":
    app.run()