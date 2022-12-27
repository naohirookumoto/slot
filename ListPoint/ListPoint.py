import sqlite3
import random

def run2(memberCombo):
    con = sqlite3.connect("list.db")
    cur = con.cursor()
    querylist = cur.execute("SELECT * FROM member").fetchall()
    max = cur.execute("SELECT MAX(hit) FROM member").fetchone()[0]
    flatFlag = True
    for row in querylist:
        # print(str(row[0]).zfill(2) + " : " + row[1] + " : " + str(row[2]))
        if max != row[2]:
            flatFlag = False
    if not flatFlag :
        while True:
            rnd = random.randint(0,len(querylist)-1)
            # print(len(querylist))
            if not querylist[rnd][2] == max:
                print(querylist[rnd][1])
                cur.execute("UPDATE member SET hit = hit + 1 WHERE No = " + str(querylist[rnd][0]))
                break
    else:
        rnd = random.randint(0,len(querylist)-1)
        # print(rnd)
        print(querylist[rnd][1])
        cur.execute("UPDATE member SET hit = hit + 1 WHERE No = " + str(querylist[rnd][0]))
    con.commit()
    if memberCombo is not None:
        memberCombo.current(querylist[rnd][0]-1)

def run():
    run2(None)

if __name__ == '__main__':
    run()