from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
all_post = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=all_post)

@app.route('/post/<num>')
def get_post(num):
    return render_template('post.html', post=all_post[int(num)-1])

if __name__ == "__main__":
    app.run(debug=True)
