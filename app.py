from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"welcome to my project"}

@app.route("/read")
def read():
    return {"payload":"read successfully"
    }

if __name__ == "main":
    app.run(debug=True)
