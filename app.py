from flask import Flask

app = Flask(__name__)
@app.route("/")
def home():
    return"HELO THIS IS MAIN PAGE <h1>hello</h1>"

if __name__=="__main__":
    app.run()    