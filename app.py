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

@app2.route("/create", methods=["POST"])
def create():
    userlist = request.args.get("usuario")
    if userlist in LISTA:
        return {
            "payload": userlist
        }
    else:
        return "no esta"
