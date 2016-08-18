from flask import *
from flask.ext.pymongo import PyMongo
import collections
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

# Mongo DB mLab configuration details
#New version
app.config['MONGO_DBNAME'] = "project_python"
app.config['MONGO_URI']= "mongodb://project:mahima@ds033015.mlab.com:33015/project_python"

#Session secret key for passing cityname from homepage to next cities page
app.secret_key ="Mahima"


#Instantiate the mongodb
mongo= PyMongo(app)

# News feed for Cities
def News(city_name):
    page =1
    #Dictionary of all the cities and their respective news website
    city_url = {"San Francisco": "http://abc7news.com/san-francisco/", "Los Angeles": "http://abc7news.com/place/los-angeles/",
    "San Diego" : "http://abc7.com/place/san-diego/", "San Jose": "http://abc7news.com/place/san-jose/"}
    '''
    Based on cityname, go to respective webpage and find first 5 news headlines
    and convert into plain text and split based on spaces and add these top 5 news headlines
    into list and return the list
    '''
    while(page < 2):
        url = city_url[city_name]
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        feed = []

        for link in soup.findAll('div', {'class':'headline' })[:5]:
            title = link.string
            news = re.split(r'\s*',title)
            news_text = ' '.join(map(str, news))
            feed.append(news_text)


        page +=1


    return feed



# Parent class, format_load method is overriden in its child classess
class Mongo_writer:
    def __init__(self, alist,city_value, menu_value,del_val):
        self.alist = alist
        self.city_value = city_value
        self.menu_value = menu_value
        self.del_val = del_val

    #To format the input data as per requirement
    def format_load(self):
        length_list = len(self.alist)
        print(length_list)
        count = length_list//4
        even=0
        self.event_dict = {}
        while(count > 0):
            print("counting")
            if (self.menu_value == "Event"):
                self.event_dict.update({self.alist[even] :["Name: " + self.alist[even], "Date: "+self.alist[even +1] , "Popular: "+self.alist[even+2], "Address: " +self.alist[even+3]]})
            elif (self.menu_value == "Resturants"):
                self.event_dict.update({self.alist[even] :["Name: " + self.alist[even], "Rating: "+self.alist[even +1] , "Cuisine: "+self.alist[even+2], "Address: " +self.alist[even+3]]})
            elif(self.menu_value == "Hotels"):
                self.event_dict.update({self.alist[even] :["Name: " + self.alist[even],"Rating: "+self.alist[even +1] , "Type: "+self.alist[even+2], "Address: " +self.alist[even+3]]})
            else:
                self.event_dict.update({self.alist[even] :["Name: " + self.alist[even], "Rating: "+self.alist[even +1] , "Type: "+self.alist[even+2], "Address: " +self.alist[even+3]]})


            count= count-1
            even = even+4
        print(self.event_dict)
        return (self.event_dict)





#Resturants class (subclass)
class Resturants(Mongo_writer):
    def __init__( self,alist, city_value, menu_details,del_val):
        super().__init__(alist, city_value, menu_details, del_val)

    #Method Overriding

    def format_load(self):
        self.data = super().format_load()

        # Either Insert the data or delete data from mongodb
        try:
            data_db = mongo.db.Cities
            for i in (self.data).keys():
                #Insert the data
                if  not self.del_val:
                    print(self.data[i])
                    data_db.update({'City_name':self.city_value}, {'$set': {'City_resturants.' + i: self.data[i]}})
                #Delete data
                else:
                    print("deleting")
                    data_db.update({'City_name':self.city_value}, {'$unset': {'City_resturants.' + i: self.data[i]}})
        except:
            print("Data collection Cities not available in mongodb")






#Events class
class Events(Mongo_writer):
    def __init__(self, alist, city_value, menu_details,del_val):
        super().__init__( alist, city_value, menu_details,del_val)


    #Method Overriding
    def format_load(self):
        self.data = super().format_load()

        #Insert the data into mongodb
        try:
            data_db = mongo.db.Cities
            for i in (self.data).keys():
                if  not self.del_val:
                    print(self.data[i])
                    data_db.update({'City_name':self.city_value}, {'$set': {'City_events.' + i: self.data[i]}})
                else:
                    print("deleting")
                    data_db.update({'City_name':self.city_value}, {'$unset': {'City_events.' + i: self.data[i]}})
        except:
            print("Data collection Cities not available in mongodb")

#Hotels class
class Hotels(Mongo_writer):
    def __init__(self, alist, city_value, menu_details,del_val):
        super().__init__( alist, city_value, menu_details,del_val )

    #Method Overriding
    def format_load(self):
        self.data = super().format_load()

        #Insert the data into mongodb
        try:
            data_db = mongo.db.Cities
            for i in (self.data).keys():
                if  not self.del_val:
                    print(self.data[i])
                    data_db.update({'City_name':self.city_value}, {'$set': {'City_hotels.' + i: self.data[i]}})
                else:
                    print("deleting")
                    data_db.update({'City_name':self.city_value}, {'$unset': {'City_hotels.' + i: self.data[i]}})
        except:
            print("Data collection Cities not available in mongodb")



#Places  sub class inherits from Mongo Writer Parent class
class Places(Mongo_writer):
    def __init__(self, alist, city_value, menu_details,del_val):
        super().__init__( alist, city_value, menu_details, del_val)

#Method Overriding
def format_load(self):
    self.data = super().format_load()

    #Insert the data into mongodb
    try:
        data_db = mongo.db.Cities
        for i in (self.data).keys():
            if  not self.del_val:
                print(self.data[i])
                data_db.update({'City_name':self.city_value}, {'$set': {'City_places.' + i: self.data[i]}})
            else:
                print("deleting")
                data_db.update({'City_name':self.city_value}, {'$unset': {'City_places.' + i: self.data[i]}})
    except:
        print("Data collection Cities not available in mongodb")






# Render home html template
@app.route('/', methods = ['POST', 'GET'])
def home():
    try:
        if request.method == "POST":  # If user selects any city name from selection box
            session['city_name'] = request.form['city_name'] # Get the name and assign it to city_name  session
            return redirect(url_for('cities'))# Redirect to cities html template whose contents changes according to selected city

    except Exception as e: #If Error in getting the cityname, then print the error
        print(e)

    return render_template("profile.html") #Renders the starting page



#Render Cities template
@app.route('/cities', methods = ['POST', 'GET'])
def cities():
    if request.method == "GET":
        user = mongo.db.Cities  # gets the mongodb and collection "Cities"
        city_name =  session['city_name']

        city_value= user.find_one({'City_name':city_name}) # queries mongodb for  selected cityname
        news_feed = News(city_name) # Call the news feed function

        # Renders cities Page with full dictionary of that city and news feed
        return render_template("city1.html",city_value = city_value, news= news_feed  )



#Add Feedback for the Application
@app.route('/contact',methods = ['POST', 'GET'])
def contact1():


    feedback = collections.OrderedDict()
    feedback_db= mongo.db.Feedback

    #Gets all feedbacks from mongodb and builds the feedback dictionary
    feedback1 = feedback_db.find()
    for feeds in feedback1:
        feedback.update(feeds)
    #Removes the mongodb objectID from feedback dictionary
    del feedback['_id']

    #If new feedback is posted, geths the user comment and user name and updates the feedback dictionary
    if request.method == 'POST':

        user= request.form['name']
        comment = request.form['comments']
        feedback.update({user:comment})
        feedback_db= mongo.db.Feedback
        feedback_db.insert({user: comment})

        #Renders contact html with feedback dictionary for display
        return render_template('contact.html', feedback= feedback)



    return render_template('contact.html', feedback= feedback)



#Admin Sign-in
@app.route('/Sign',methods = ['POST', 'GET'])
def Sign_in():
    try:
        if request.method == "POST":  # If user enters the data

            username = request.form['Username'] # Get the username
            password = request.form['Password'] # Get the password
            admin_db= mongo.db.admin
            #actual_password = admin_db.find_one({'Username' : username})

            #if(actual_password['Password'] == password):
            if((username == "Admin") and (password == "Admin")):
                print("true")
                return render_template("admin.html", login = "true")
            else:
                print("false")
                return render_template("admin.html", login = "false")


    except Exception as e:
        print(e)

    return render_template("admin.html", login = "false")


#Admin Page
@app.route('/details',methods = ['POST', 'GET'])
def details():
    try:
        if request.method == "POST": # If user enters the data
            details = ({ 'data': request.get_json() })

            city_value = details["data"]["uid"][1] # Gets the city Name
            menu_value = details["data"]["uid"][2] # Gets the Menu Name
            del_val = details["data"]["uid"][3] # Gets if the request is for delete or add/update
            menu_details = details["data"]["uid"][0][0] #Gets the entry details list
            len_menu= len(menu_details) #Gets the length of the entry details list
            final_details = [[]]
            value_list = []


            #Properly formats the data in the list
            for i in range(len_menu):
                for j in (menu_details[i].values()):
                    value_list.append(j)
            print((value_list))

            #Create an object of events class for tetsing
            if(menu_value == "Event"):
                e= Events(value_list,city_value, menu_value,del_val)
                e.format_load()

            elif(menu_value == "Resturants"):
                r= Resturants(value_list,city_value, menu_value,del_val)
                r.format_load()

            elif(menu_value == "Hotels"):
                h= Hotels(value_list,city_value, menu_value,del_val)
                h.format_load()

            else:
                p= Places(value_list,city_value, menu_value)
                p.format_load()

    except Exception as e:
        print(e)

    return render_template("admin.html", login = "true")







if __name__ == '__main__':
    app.run()
