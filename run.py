# webサーバを立ち上げる際に実行するファイル

from app.app import app

if __name__ == "__main__":
    app.run(host='0.0.0.0')