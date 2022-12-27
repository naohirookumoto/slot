import tkinter
import tkinter.ttk as module
import sqlite3
import Ans
import PrintList
import ListPoint

con = sqlite3.connect("list.db")
cur = con.cursor()
querylist = cur.execute("SELECT name FROM member").fetchall()

root = tkinter.Tk()
root.title("ListPoint")
root.geometry("200x120")

memberCombo = module.Combobox(root,state='readonly')
memberCombo["values"] = querylist
memberCombo.current(0)
memberCombo.pack()

addButton = module.Button(text='加点',command=lambda:(Ans.run2(memberCombo.current()+1,1)))
addButton.pack()

minusButton = module.Button(text='減点',command=lambda:(Ans.run2(memberCombo.current()+1,-1)))
minusButton.pack()

printButton = module.Button(text='表示',command=lambda:(PrintList.run()))
printButton.pack()

pointButton = module.Button(text='当てる',command=lambda:(ListPoint.run2(memberCombo)))
pointButton.pack()

root.mainloop()