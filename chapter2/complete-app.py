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

#the Flask dws can also be started programmatically by invoking the app.run() method.
'''if __name__ == '__main__':
    app.run()
'''
#using flask run is more practical. the above is used in certain occasions suchh as unit testing.
