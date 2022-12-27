# 正N角形を描画します。Nとサイズを指定してください
import turtle

# N角形
kaku:int = 20
# 描画サイズ
size:int = 30

angle:int = 360 / kaku
kame = turtle.Turtle()
kame.home()
i:int = 0
while True:
    print(f'q：終了{i}')
    if i == 0:
        arg = ''
    if arg == 'q':
        break
    else:
        for i in range(kaku):
            kame.forward(size)
            kame.left(angle)
    arg:str = input()
        