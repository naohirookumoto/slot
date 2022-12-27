# 一筆書きの正N角形
import turtle
size:int = 100
kame = turtle.Turtle()
kame.speed(10)
i:int = 0
# リストにセットした正N角形を順番に描画
kaku_l = [5,7,9,11,13,15,17,19]
while True:
    print('q：終了')
    if i == 0:
        arg = ''
    if arg == 'q':
        break
    else:
        for kaku in kaku_l:
            for i in range(kaku):
                kame.forward(size)
                kame.left(360 - (720 / kaku))
            # 次のN角形を描画し始める位置調整
            kame.penup()
            kame.home()
            kame.left(90)
            kame.forward((size * (kaku)) / 17)
            kame.right(90)
            kame.pendown()
    arg:str = input()
        