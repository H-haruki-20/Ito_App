# Ito
### itoというボードゲームをwebブラウザで遊べるようにしました．
### Flaskに慣れるための練習用です．
## 内容
複数人で遊ぶゲーム．
お題にそうようなことを1から100までの表示された乱数に合わせていう．

## 仕様,機能
- homepage 
- play mode
	- プレイ人数を入れる．(2から5人とか)
	- プレイヤー1の名前を入力... をプレイ人数分繰り返す．
	- お題をランダムに表示
	- 他の人と被らないように1から100までの乱数を表示する．
	- 制限時間5minスタート
	- 答えを入力
	- 結果発表 (正解 or 間違い)

まずはここまで1セットで実装してみる．

## 実装
バックはFlask(python),フロントはJSとHTMLで書いてます．
