# import necessary libraries
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import sys
import json
from flask_cors import CORS


# create instance of Flask app
app = Flask(__name__, static_url_path='/static')
CORS(app)

app.config['MONGO_DBNAME']='therapists'
app.config['MONGO_URI']="mongodb://localhost:27017/therapists"
mongo=PyMongo(app)


@app.route("/")
def home():
   return render_template("index.html")

@app.route("/about")
def about():
   return render_template("/about.html")

@app.route("/json2html")
def json2html():
   return render_template("/data.html")



@app.route("/data", methods= ['GET', 'POST', 'OPTIONS'])
def data():
    therapists=mongo.db.ca_therapists
    output = []
    # test = []
    for therapist in therapists.find({}):
        output.append({"coordinates":therapist["coordinates"], 'name':therapist['name'], 'photo':therapist['photo'], 'website':therapist['website'], 'issues':therapist['issues'], 'treatment approaches':therapist['treatment approaches'], 'specaialties':therapist['specialties']})
        # test.append({"coordinates":therapist["coordinates"]})
    return jsonify(output)

# output.append({"id":therapist["id"],"coordinates":therapist["coordinates"], 'name':therapist['name'], 'issues':therapist['issues'], 'specaialties':therapist['specialties'], 'photo':therapist['photo'], 'phone number':therapist['phone number'], 'treatment approaches':therapist['treatment approaches'], 'website':therapist['website']})
# return jsonify(output[0:800])
if __name__ == "__main__":
   app.run(debug=True)