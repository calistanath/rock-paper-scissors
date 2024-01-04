from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choices = ['rock', 'paper', 'scissors']
    user= request.form['choice']
    computer= random.choice(choices)

    result = determine_winner(user, computer)

    return render_template('result.html', user=user, computer=computer, result=result)

def determine_winner(user, computer):
    if user == computer:
        return 'It\'s a tie!'
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'paper' and computer == 'rock') or
        (user == 'scissors' and computer == 'paper')
    ):
        return 'You win!'
    else:
        return 'You lose!'

if __name__ == '__main__':
    app.run(debug=True)
