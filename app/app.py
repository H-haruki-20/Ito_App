from flask import Flask, render_template, request
from flask import *
import random
from flask_sqlalchemy import SQLAlchemy

# Flaskオブジェクトの生成
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/playmode",methods=['GET'])
def play():
    return render_template("play_number.html")

@app.route("/playmode-number",methods=["POST"])
def playmodenumberpost():
    print("データを受け取りました．")
    req = request.form["data1"]
    return render_template("play_name.html",player_number = req)

@app.route("/playmode-name",methods=["POST"])
def playmodenamepost():
    number = request.form["number"]
    number = int(number)
    name = []
    num = []
    for i in range(number):
        name.append(request.form["player" + str(i+1)])
        num.append(random.randint(1,100))
        print(name[i], num[i])
    
    return render_template("player1.html",play = name, num = num, player_number=number)

# カウントダウンタイマーがスタートする．(game.htmlで表示させる)
@app.route("/gamestart",methods=["GET"])
def gamestart():
    return render_template("game.html")

@app.route("/answer",methods=["GET"])
def answer():
    return render_template("answer.html")


#おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)