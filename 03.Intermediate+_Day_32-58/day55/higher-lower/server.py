from flask import Flask
import random

app = Flask(__name__)
random_number = random.randint(0, 9)
print(random_number)

@app.route('/')
def display():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/l2SpYSNrKPONySXYY/giphy.gif?cid=ecf05e47ijrxfzfytxgn28pvgyaqge67ln6jlod5n4s0l6pj&ep=v1_gifs_search&rid=giphy.gif&ct=g">')


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < random_number:
        return ('<h1 style="color: red">Too low, try again!</h1>'
                '<img src="https://media.giphy.com/media/rG7GdjuLtGRlHZpi0K/giphy.gif?cid=ecf05e47nvym09nrybh1f4c5ehz2g8rnmt4lqxhicxa5jxlj&ep=v1_gifs_search&rid=giphy.gif&ct=g">')
    elif guess > random_number:
        return ('<h1 style="color: purple">Too high, try again!</h1>'
                '<img src="https://media.giphy.com/media/s8C0AlyAfcElpgec1V/giphy.gif?cid=790b7611w176yljrad3ywi3kvgkr07rhq9biwwf10ajb0ozo&ep=v1_gifs_search&rid=giphy.gif&ct=g">')
    else:
        return ('<h1 style="color: green">You found me!</h1>'
                '<img src="https://media.giphy.com/media/Z9tvqoD1SEQcomTVaK/giphy.gif?cid=ecf05e47cb03csm0nvbez33442vicd2gag8wltgdl4y4tdpi&ep=v1_gifs_search&rid=giphy.gif&ct=g">')

if __name__ == '__main__':
    app.run(debug=True)