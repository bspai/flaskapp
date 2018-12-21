from flask import Flask
from modules.api1 import api1 
from modules.api2 import api2
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route("/api1")
def a1():
    return api1.run()

@application.route("/api2")
def a2():
    return api2.run() 

if __name__ == "__main__":
    application.run(host='0.0.0.0')
