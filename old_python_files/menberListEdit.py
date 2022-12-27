# メンバーリストエディター
# CSVファイルの読み書き作成課題
print("メンバーリストエディターを起動します。")

# ○アプリケーション準備
# ファイル名の入力
fileName = input("ファイル名を入力してください。")

# 書き込みモードの選択
while True:
  print("[1]新規作成[2]追記モード")
  cmd = input(":")
  # 1か2の時
  if cmd in ["1","2"] :
    mode = cmd
    break
  print("正しいコマンドを入力してください。")
print(mode)

# ○データ生成
dataList = []

# 追記モード時
if mode == "2":
  # 既存csvからデータを取り込む
  with open(fileName,"r",encoding="utf-8") as data:
    # CSVデータが,区切りでリスト型に変換
    dataList = data.read().split(",")

# メンバーを追加するか？終了するか？
while True:
  print("現在のメンバーは")
  print(dataList)
  print("[1]メンバー追加[q]終了")
  cmd = input(":")
  match cmd:
    case "1":
      print("追加するメンバーの氏名を入力してください。")
      name = input("氏名：")
      dataList.append(name)
    case "q":
      break
    case _:
      print("正しいコマンドを入力してください。")

# ○終了処理
# 書き込み処理
with open(fileName,"w",encoding="utf-8") as csv:
  # dataListをCSV形式のデータに変換
  inputText = ",".join(dataList)
  # CSVへ書き込み
  csv.write(inputText)

print("メンバーリストエディターを終了します。")