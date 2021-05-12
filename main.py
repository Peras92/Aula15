from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutme/")
def about_me():
    return render_template("about me.html")

@app.route("/portefolio/")
def portfolio():
    return render_template("portefolio.html")

@app.route("/portefolio/fakebook/")
def fakebook():
    return render_template("Fakebook.html")

if __name__ == '__main__':
    app.run(use_reloader=True)