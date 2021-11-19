from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'asdfhpoiewrqpoiehh'

# localhost:5000 route
@app.route('/')
def index():
    language_list = ['Select','C#', 'C++', 'Java', 'JavaScript', 'Python']
    location_list = ['Select', 'Seattle', 'New York', 'Chicago', 'San Jose']
    return render_template('index.html', languages = language_list, locations = location_list)

# post request
@app.route('/process', methods=["POST"])
def process():

    # store data in temporary storage
    session['name'] = request.form['name']
    session['dojo-location'] = request.form['dojo-location']
    session['fav-language'] = request.form['fav-language']
    session['comments'] = request.form['comments']
    session['age'] = request.form['age']
    session['program'] = request.form['program']

    # send to another route to display data
    return redirect('/result')

# route that displays form inputs
@app.route('/result')
def result():

    return render_template('/result.html')

if __name__== '__main__':
    app.run(debug=True)