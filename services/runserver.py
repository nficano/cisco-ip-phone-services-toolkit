from flask import Flask, make_response
app = Flask(__name__)

@app.route("/api/services")
def services():
    pass

@app.route("/api/authentication")
def authentication():
    return "AUTHORIZED"

@app.route("/api/directory")
def directory():
    return ""

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
