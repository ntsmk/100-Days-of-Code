from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # todo need to fill out here. use agefy and genderfy API. take input from URL path
    name = # todo capitalize it
    gender =
    age =
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)