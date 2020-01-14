from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World <h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1> Hello , {}! </h1>'.format(name)


#We have not included the development web server yet.


#to run development web server.(Linux) 
#Run : 
#        export FLASK_APP=complete-app.py in terminal.
#    then : 
#        flask run

#to run development web server.(Windows) 
#Run : 
#        set FLASK_APP=complete-app.py in terminal.
#    then : 
#        flask run