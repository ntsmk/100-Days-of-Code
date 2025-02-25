from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    my_name = "Nat"
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, my_name=my_name, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)