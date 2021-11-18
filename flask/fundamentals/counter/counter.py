from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'awefh;oidfhapoehfowefkasdffa'

@app.route('/')
def index():
    if 'visits' not in session:
    # checks to see if key exists in session yet, if not the variable is set to 1
        session['visits'] = 1
    else:
    # if yes (user has already visited page once), the variable count goes up by 1)
        session['visits'] += 1

    return render_template("index.html")

@app.route('/add_two')
def count_by_twos():
    if 'visits' not in session:
    # checks to see if key exists in session yet, if not the variable is set to 1
        session['visits'] = 1
    else:
    # if yes (user has already visited page once), the variable count goes up by 1)
        session['visits'] += 2

    return render_template("index.html")

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)