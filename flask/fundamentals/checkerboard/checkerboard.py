from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard_1():
    return render_template("index.html")

@app.route('/4')
def checkerboard_2():
    return render_template("index2.html")

@app.route('/<int:x>/<int:y>')
def checkerboard_3(x,y):
    return render_template("index3.html", x=x, y=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def checkerboard_4(x,y, color1, color2):
    return render_template("index4.html", x=x, y=y, color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)

