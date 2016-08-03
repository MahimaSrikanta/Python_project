import os
import pickle

from flask import *
from pymongo import MongoClient


def connect():
    connection = MongoClient("ds033015.mlab.com", 33015)
    handle = connection["project_python"]
    handle.authenticate("project", "mahima")
    return handle


app = Flask(__name__)

# Mongo DB mLab configuration details
# app.config['MONGO_DBNAME'] = "project_python"
# app.config['MONGO_URI'] = "mongodb://project:mahima@ds033015.mlab.com:33015/project_python"

# Session secret key for passing cityname from homepage to next cities page
app.secret_key = "Mahima"

# Instantiate the mongodb
# mongo = PyMongo(app)
mongo = connect()
user = mongo.Cities  # gets the mongodb and collection "users"


# Resturants class
class Resturants(dict):
    def __init__(self):
        self = dict()

    def saveCity(self):
        # Save the dictionary into file
        Resturants_File = open('resturants.txt', 'wb')
        pickle.dump(self, Resturants_File)
        Resturants_File.close()

    def addCity(self, key, value):
        self.update({key: value})
        self.saveCity()


# Events class
class Events:
    def __init__(self):
        self = dict()


# Hotels class
class Hotels:
    def __init__(self):
        self = dict()


class Cities(Resturants, Events, Hotels):
    def __init__(self):
        self = dict()


# Render home html template
@app.route('/', methods=['POST', 'GET'])
def home():
    try:
        if request.method == "POST":  # If user selects any city name from selection box

            session['city_name'] = request.form['city_name']  # Get the name and assign it to city_name  session

            return redirect(
                url_for('cities'))  # Redirect to cities html template whose contents changes according to selected city
    except Exception as e:
        print(e)

    return render_template("profile.html")


# Render Cities template
@app.route('/cities', methods=['POST', 'GET'])
def cities():
    if request.method == "GET":
        user = mongo.db.Cities  # gets the mongodb and collection "users"
        city_name = session['city_name']
        print(city_name)
        city_value = user.find_one({'City_name': city_name})  # mongodb return a dictionary

    return render_template("city1.html", city_value=city_value)


# Remove the "debug=True" for production
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))

    app.run(host='localhost', port=port, debug=True)
