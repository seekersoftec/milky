from flask import Flask,request,jsonify,render_template
from app_api import api

app = Flask(__name__)
app.config["DEBUG"] = True

# home
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


# 404 page not found
@app.errorhandler(404)
def page_not_found():
    return render_template("404.html")

# run app
app.run()