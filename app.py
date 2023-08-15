from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    return {"payload":"hack-1 finished"}

@app.route("/read")
def read():
    return {"payload":"read successfully"
    }

@app.route("/create", methods=["POST"])
def create():
    return {"payload":"create successfully"
    }


if __name__ == "main":
    app.run(debug=True)

