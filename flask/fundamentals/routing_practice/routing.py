from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_hello(name):
    return f"Hi {name.capitalize()}!"

@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num,word):
    return (word * num)

@app.route('/%')
def error_message():
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(debug=True)