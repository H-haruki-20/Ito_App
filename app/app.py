from flask import Flask, render_template, request

# Flaskオブジェクトの生成
app = Flask(__name__)

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
    name = request.form["player1"]
    return f"{name}さん，こんにちは！"


#おまじない
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)