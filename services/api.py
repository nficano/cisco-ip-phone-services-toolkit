from flask import Flask, make_response
from ciscoipphone.services import Menu
app = Flask(__name__)

@app.route("/api/services")
def services():
    pass

@app.route("/api/authentication")
def authentication():
    return "AUTHORIZED"

@app.route("/api/directory")
def directory():
    response = make_response()
    response.mimetype = 'text/xml'
    menu = Menu(prompt="Select a directory")
    menu.add('My Contacts', 'http://192.168.1.142:5000/directory/my_contacts')
    menu.add('Businesses', 'http://192.168.1.142:5000/directory/businesses')
    menu.add('Coworkers', 'http://192.168.1.142:5000/directory/coworkers')
    menu.add('Family', 'http://192.168.1.142:5000/directory/family')
    response.data = menu.serialize()
    return response

@app.route("/api/idle")
def idle():
    return ""

@app.route("/api/information")
def information():
    return ""

@app.route("/api/messages")
def messages():
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
