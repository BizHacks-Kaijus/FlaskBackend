from flask import Flask, render_template, flash, request
from content_management import Content

TOPIC_DICT  = Content()
# the folder static is for the files for css, img, js files
# the templates folder is for html files 
# keep all python files in same directoory as the flaskbackend.
# To start, run flaskbackend

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("base.html")

@app.route('/index/')
def index():
    flash("flash test!")
    flash ("????")
    flash("asd")
    return render_template("index.html", TOPIC_DICT = TOPIC_DICT)

@app.errorhandler(404)
def page_not_found(e):
    return "error 404"

@app.errorhandler(405)
def method_not_found(e):
    return "error 405"

@app.route('/login/', methods = ["GET", "POST"])
def login_page():
    return render_template("login.html")

@app.route('/handle_data', methods =['POST']) 
def handle_data():
    productName = request.form['pname']
    uploadFile = request.form['uploadedFile']
    categoryType = request.form['category']
    description = request.form['descrip']
    return request.form['uploadedFile']
    #return '{} {} {}'.format(productName, uploadFile, categoryType,description)
    #request.form['pname'] request.form['uploadedFile'],request.form['category'],request.form['descrip']

if __name__ == "__main__":
    app.run()
