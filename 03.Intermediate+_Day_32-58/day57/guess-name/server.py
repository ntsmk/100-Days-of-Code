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

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)

if __name__ == "__main__":
    app.run(debug=True)