# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def home():

    return render_template("index.html")

# create route that renders dct.html
@app.route("/dct")
def dct():

    return render_template("dct.html")


# create route that renders NavieBayes.html
@app.route("/naivebayes")
def naivebayes():

    return render_template("naivebayes.html")

# # create route that renders tableau.html
@app.route("/tableau")
def tableau():

    return render_template("tableau.html")


if __name__ == "__main__":
    app.run(debug=True)
