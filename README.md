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

 			pip freeze requirements.txt

 




	#a convention for virtual envs is to call them venv-name