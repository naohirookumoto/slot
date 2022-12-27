import sqlite3
import random
def run():
    con = sqlite3.connect("list.db")
    cur = con.cursor()
    querylist = cur.execute("SELECT * FROM member").fetchall()
    print("No : 氏名 : 回数 : 解答")
    for row in querylist:
        print(str(row[0]).zfill(2) + " : " + row[1] + " : " + str(row[2])+ " : " + str(row[3]))
if __name__ == '__main__':
    run()