from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def blue_boxes():
    return render_template("index.html")

@app.route('/play/<int:x>')
def create_box(x):
    return render_template("index.html", x=x)

@app.route('/play/<int:x>/<string:color>')
def color_boxes(x, color):
    return render_template("index.html", x=x, color=color)

if __name__=="__main__":
    app.run(debug=True)