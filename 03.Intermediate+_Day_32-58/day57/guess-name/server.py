from flask import Flask, render_template
import requests

age_endpoint = "https://api.agify.io?name="
gender_endpoint = "https://api.genderize.io?name="
# response_age = requests.get(url=age_endpoint+"natsumi")
# response_gender = requests.get(url=gender_endpoint+"natsumi")
# print(response_age.json()['age']) # 38
# print(response_age.json()['name'].title()) # capitalized first letter\
# print(response_gender.json()['gender']) # female

app = Flask(__name__)
@app.route('/')
def display():
    return '<h1>Enter your name. /guess/(your name)</h1>'

@app.route('/guess/<string:entered_name>')
def result(entered_name):
    name = entered_name.title()
    gender = requests.get(url=gender_endpoint+name).json()['gender']
    age = requests.get(url=age_endpoint+name).json()['age']
    return render_template("index.html", name=name, gender=gender, age=age)

if __name__ == "__main__":
    app.run(debug=True)