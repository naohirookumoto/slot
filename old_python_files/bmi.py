from tkinter import *
from tkinter import ttk

# print('身長( m )？')
# h = float(input())
# print('体重( kg )？')
# w = float(input())


root = Tk()
root.title('BMI判定')
root.resizable(False, False)
frame1 = ttk.Frame(root, padding=(32))
frame1.grid()
# ラベル（身長）
hight_label = ttk.Label(frame1, text='身長', padding=(5, 2))
hight_label.grid(row=0, column=0, sticky=E)

# ラベル（体重）
weight_label = ttk.Label(frame1, text='体重', padding=(5, 2))
weight_label.grid(row=1, column=0, sticky=E)

# ラベル（結果）
judg_label = ttk.Label(frame1, text='結果', padding=(5, 2))
judg_label.grid(row=2, column=0, sticky=E)

# 入力、身長
hight = DoubleVar()
hight_input = ttk.Entry(
    frame1,
    textvariable=hight,
    width=20
    )
hight_input.grid(row=0, column=1)

# 入力、体重
weight = DoubleVar()
weight_input = ttk.Entry(
    frame1,
    textvariable=weight,
    width=20
    )
weight_input.grid(row=1, column=1)


def cal(self):
    h = self.hight_input.get()
    w = self.weight_input.get()
    bmi = h / w ** 2
    return bmi

# ボタン用フレーム
frame2 = ttk.Frame(frame1, padding=(0, 5))
frame2.grid(row=3, column=1, sticky=W)
# 計算ボタン
button1 = ttk.Button(frame2, text='BMI計算')
button1.bind("", cal())
    # command = (bmi = call())
# 
button1.pack(side=LEFT)



hight = float(hight)
weight = float(weight)
print(f'hight:{hight}, {type(hight)}')
print(f'weight:{weight}, {type(weight)}')

bmi = weight / (hight ** 2)
# bmi = 25.1
bmi_s = '{:.1f}'.format(bmi)

# 判定
if bmi < 18.5:
     judg = 'やせ型'
elif bmi < 25.0:
     judg = '標準'
elif bmi < 30.0:
     judg = '肥満'
else:
     judg = '高度な肥満'

msg = f'あなたは{judg}体型です。BMI値：{bmi_s}\n'
print(msg)

# ラベル（判定結果）
result_label = ttk.Label(frame1, text=msg, padding=(5, 2))
result_label.grid(row=2, column=1, sticky=E)

root.mainloop()
