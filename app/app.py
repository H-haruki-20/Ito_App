from os import sep
from flask import Flask, render_template, request
from flask import *
import random
# from flask_sqlalchemy import SQLAlchemy
import csv
import pandas as pd

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

    # csvファイルを作成し，プレイヤーのデータを格納する．
    with open("data.csv","w") as csv_file:
        fieldnames = ["Name", "Number"]
        writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
        writer.writeheader()
        for i in range(number):
            writer.writerow({"Name":name[i],"Number":num[i]})

    return render_template("player1.html",play = name, num = num, player_number=number)

# カウントダウンタイマーがスタートする．(game.htmlで表示させる)
@app.route("/gamestart",methods=["GET"])
def gamestart():
    return render_template("game.html")

@app.route("/answer",methods=["GET"])
def answer():
    # pandasでdata.csvファイルを読み取り，それをjsonにする．
    # data.csvからプレイヤー情報をjson形式で表し，そのjsonをrender_templateでanswer.htmlに送る．
    csv_data = pd.read_csv("data.csv",sep=",")
    print(csv_data)
    print(type(csv_data))
    # あくまでもjson形式の文字列
    json_data = csv_data.to_json()
    
    return render_template("answer.html",json_data=json_data)


#おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)