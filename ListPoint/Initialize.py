import sqlite3
import csv
import os
def run():

    print("初期化csvを指定してください。")
    print("CSV名" + " : " + "説明")
    # index.csv読み込み選択肢を表示
    with open("InitializeCSV\\index.csv", "r" ,encoding="utf-8") as csv1:
        reader = csv.reader(csv1)
        for row in reader:
            print(row[0] + " : " + row[1])

    #コンソール入力
    cmd = input("csvFileName:")
    csvFilePath = "InitializeCSV\\" + cmd + ".csv"
    newFileFlag = not os.path.isfile("list.db")
    con = sqlite3.connect("list.db")
    cur = con.cursor()
    if not newFileFlag:
        cur.execute("DROP TABLE member")
    cur.execute('''CREATE TABLE member(No INTEGER,name TEXT,hit INTEGER,ans INTEGER)''')
    with open(csvFilePath, "r" ,encoding="utf-8") as csv1:
        reader = csv.reader(csv1)
        for row in reader:
            cur.execute("INSERT INTO member VALUES (" + row[0] + "," + row[1] + "," + row[2] + "," + row[3] + ")")
    con.commit()
if __name__ == '__main__':
    run()