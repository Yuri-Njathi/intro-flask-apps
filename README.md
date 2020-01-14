# intro-flask-apps
#Herein lie notes.
This introductory repository is based on the book :

Flask Web Development : Developing Web Applications with Python : Miguel Grinberg 2nd edition. (It is an O'Reilly book, Good job O'Reilly)

#Chapter 1 : Flask is a small framework : actually more of a microframework.
			:Flask is designed as an extensible framework.
			:It provides a solid core with the basic services, while extensions provide the rest.


			Flask dependencies : 
			1) #Werkzeug# ie routing,debugging and Web Server Gateway Interface(WSGI)
			2) #Jinja2# template support
			3) #Click# command-line-intergration.

The dependencies were authored by Flask author : Armin Ronacher.(https://g.co/kgs/9b8qJm)

Flask has no native support for accessing databases,validating web forms , authentication users or other high-level tasks.

As a developer , you have the power to pick or create necessary extensions. In larger frameworks this choices are made for you.

#Virtual Environment#
	Installs the Python # interpreter on a Ubuntu Linux system:

			sudo apt-get install python3-venv

	Create a virtual-environment-name:

			python3 -m venv venv-name

			or

			virtualenv venv-name
	#a convention for virtual envs is to call them venv-name

	To activate the virtual environment : 

			source venv-name/bin/activate (Linux/Mac-Os)

						or

			venv\Scripts\activate (Windows)

	To deactivate : 
			deactivate.



	#It is possible to use a virtual-env without activating it.(To be revisited)
	Example : start a python console for venv-name by running :
			venv/bin/python (Linux/Mac-Os)
						or
			venv\Scripts\python (Windows)

#I'm using python 3.6.9


#installing Python Packages with pip.
 
 activate venv as above

 			pip install flask

 create a requirements.txt for that environment. 

 			pip freeze -> requirements.txt


#Chapter 2
#Write and run your first web application.

#Initialization.
All flask apps must create an application instance.
The web server passes all requests it receives from clients to this object for handling , using a protocal called Web Server Gateway Interface(WSGI pronounced 
"wiz-ghee")

The application instance is an object of class Flask, usually created as follows : 
		
		from flask import Flask
		app = Flask(__name__)

#__name__ to be revisited.
#to initialize an application to be revisited.

#Routes and View Functions.
A client (web browser eg chrome ,mozilla or edge) sends requests to the web server, they send requests to the Flask application instance.

A route is an association between a URL and a fuction that  handles it.

One can define a route in a Flask application through the app.route decorator exposed by the application instance. 
Example :

	@app.route('/')
	def index():
		return '<h1> Hello World! </h1>'

#Decorators are a standard feature of Python langauge.They are usually used to register functions as handler functions to be invoked when certain events occur.

#another route method is app.add_url_rule()
	def index():
		return '<h1>Hello World!</h1>'	
	app.add_url_rule('/', 'index', index)

#functions like index() : handle application URLs are called view functions.
(I.e. if I visit vizetu.com, def index() will be triggered.)



#URLS for services.
The url for your facebook profile page has the format https://www.facebook.com/<your-name>, which includes your username, making it different for every user.
	@app.route('/user/<name>')
	def user(name):
		return '<h1> Hello , {}! </h1>'.format(name)

Flask supports the types string,int,float and path for routes.
The path type is a special string type that can include forward slashes, unlike the string type.

#Complete Application : - code in chapter2/complete-app.py

#We have not included the development web server yet.





	