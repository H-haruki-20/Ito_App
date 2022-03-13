from crypt import methods
from flask import Flask, render_template, request

# Flaskオブジェクトの生成
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/playmode",methods=["GET"])
def play():
    return render_template("play.html")

#おまじない
if __name__ == "__main__":
    app.run(debug=True)