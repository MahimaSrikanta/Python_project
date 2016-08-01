from flask import *
from flask.ext.pymongo import PyMongo
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Mongo DB mLab configuration details
app.config['MONGO_DBNAME'] = "project_python"
app.config['MONGO_URI']= "mongodb://project:mahima@ds033015.mlab.com:33015/project_python"

#Session secret key for passing cityname from homepage to next cities page
app.secret_key ="Mahima"

#Instantiate the mongodb
mongo= PyMongo(app)


'''
@app.route('/')
def index():
    return 'Hello'

# To get the varibale form the url , user specific profiles
@app.route('/profile/<user>')
def profile(user):
    return "Hey %s" %user

# Get and Post methods
@app.route('/hi', methods = ['POST', 'GET'])
def hi():
    if request.method =='POST':
        return " Post method"
    else:
        return "Get method"

'''


#Resturants class
class Resturants (dict):
    def __init__(self):
        self= dict()

    def saveCity(self):
        # Save the dictionary into file
        Resturants_File = open('resturants.txt', 'wb')
        pickle.dump(self, Resturants_File)
        Resturants_File.close()

    def addCity(self, key, value):
        self.update({key: value})
        self.saveCity()

#Events class
class Events:
    def __init__(self):
        self= dict()


# Hotels class
class Hotels:
    def __init__(self):
        self= dict()


class Cities(Resturants, Events, Hotels):

    def __init__(self):
        self = dict()



# Render home html template
@app.route('/', methods = ['POST', 'GET'])
def home():
    try:
        if request.method == "POST":  # If user selects any city name from selection box

            session['city_name'] = request.form['city_name'] # Get the name and assign it to city_name  session

            return redirect(url_for('cities'))# Redirect to cities html template whose contents changes according to selected city
    except Exception as e:
        print(e)

    return render_template("profile.html")

#Render Cities template
@app.route('/cities', methods = ['POST', 'GET'])
def cities():
    if request.method == "GET":
        user = mongo.db.Cities  # gets the mongodb and collection "users"
        city_name =  session['city_name']
        print(city_name)
        city_value= user.find_one({'City_name':city_name}) # mongodb return a dictionary




    return render_template("city1.html",city_value = city_value )

#Add details to mongodb
'''
@app.route('/add')
def add():
    user= mongo.db.users  # gets the mongodb and collection "users"
    user.insert({'name':'San Franscisco', 'language': 'python'})
    user.insert({'name':'San jose', 'language': 'english'})
    user.insert({'name':'Las Vegas', 'language': 'hindi'})
    return "Added"

#Query from mongodb
@app.route('/find')
def find():
    user = mongo.db.users  # gets the mongodb and collection "users"
    san_jose= user.find_one({'name': 'San jose'}) # mongodb return a dictionary
    return san_jose['name'] + san_jose['language']

'''

# News feed for SanFranscisco
'''
def sanFranscisco():
    page =1
    while(page < 2):
        url = 'http://abc7news.com/san-francisco/'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('div', {'class':'headline' }):
            title = link.string
            #print(title)
        page +=1


sanFranscisco()
'''



if __name__ == '__main__':
    '''
    print(" \n \n \t\t  WELCOME TO FOOD EXPRESS \n")
    res = Resturants()
    hotel_name = input(" Enter the resturants name  \n ")
    hotel_address = input("Enter the resturant address\n")
    res.addCity(hotel_name,hotel_address )
    '''

    app.run()
