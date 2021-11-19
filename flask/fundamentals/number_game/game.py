from flask import Flask, render_template, redirect,request, session
app = Flask(__name__)
app.secret_key = 'hidofoih3rh12400dfk'

import random

@app.route('/')
def index():
    session['random'] = random.randint(1,100)
    print(f"Random Number: {session['random']}")
    return render_template("index.html")

@app.route('/guess', methods=["POST"])
def guess():
    # take guess from form and put into temporary storage called session

    session['guess'] = request.form['guess']
    print(f"Guess: {session['guess']}")

    return redirect('/results')

@app.route('/results')
def results():
    if int(session['guess']) == session['random']:
        return render_template('results.html')
    elif int(session['guess']) > session['random']:
        # too high
        return render_template('tooHigh.html')
    elif int(session['guess']) < session['random']:
        # too low
        return render_template('tooLow.html')



if __name__ == "__main__":
    app.run(debug=True)