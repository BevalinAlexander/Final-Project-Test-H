# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(
    __name__,
    template_folder="templates"
)


# # Set variables
# name = "Aaron"
# hobby = "Baseball"


# create route that renders index.html template
@app.route("/")
def index():

    return render_template("index.html")


# create route that renders NavieBayes.html
@app.route("/NaiveBayes")
def NaiveBayes():

    return render_template("NaiveBayes.html")

# # create route that renders tableau.html
# @app.route("/tableau")
# def tableau():

#     return render_template("tableau.html")

# # create route that renders dct.html
# @app.route("/dct")
# def tableau():

#     return render_template("dct.html")


if __name__ == "__main__":
    app.run(debug=True)
