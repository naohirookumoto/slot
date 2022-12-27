import sqlite3
import random


def run2(no,num):
    con = sqlite3.connect("list.db")
    cur = con.cursor()
    cur.execute("UPDATE member SET ans = ans + " + str(num) + " WHERE No = " + str(no)) 
    con.commit()
def run():
    no = input("対象のNoを入力してください。")
    run2(no,1)

if __name__ == '__main__':
    run()