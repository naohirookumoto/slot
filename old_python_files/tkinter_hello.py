import tkinter
# 初期化メソッド
root = tkinter.Tk()
# ウィンドウのタイトルを設定
root.title("Hello World!!")
# ウィンドウのサイズを設定
root.geometry("800x600")
# 独自の関数を定義
# push : ボタンが押された時
def push(count):
  print("ボタン押下")
  count[0] +=1
  lb01.configure(text=str(count[0]) + "ボタン押下")
# カウント用変数
count = [0]
# ラベルの初期化メソッド
lb01 = tkinter.Label(text="Hello World!!")
# ボタンの初期化メソッド
but01 = tkinter.Button(text="ボタン",command=lambda:push(count))
# ウィンドウに設置
lb01.pack()
but01.pack()
# GUI受付開始
root.mainloop()