# =================
# 反復処理
# =================
import random
# import numpy as np
# 九九 step1
# for i in range(1, 10):
#     print(f'{i}の段')
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')

# 九九 step4
#   │ 1  2  3  4  5  6  7  8  9
# ──┼─────────────────────────────
# 1 │ 1  2  3  4  5  6  7  8  9
# 2 │ 2  4  6  8  10 12 14 16 18
# 3 │ 3  6  9  12 15 18 21 24 27
wide = 10
sp = ' '
bar = '|'
hl = '─'
# １桁なら数字の頭にスペースをwide個、２桁なら数字の頭にスペースを１桁よりも１つ少なく追加して返却
# 引数：数値型（Int,Str）
# 戻り値の型：Str型
def line_up(x):
    if type(x) == int:
        x = str(x)
    if len(x) == 1:
        x = f'{sp*wide}{x}'
    elif len(x) == 2:
        x = f'{sp*(wide - 1)}{x}'
    return x
# 列見出し
col_head = f'{sp*3}{bar}'
# 行見出し
row_head = f'{sp*2}{bar}'

# 見出し行と区切り線
for i in range(1, 10):
    col_head = col_head + line_up(i)
print(f'\n\n{col_head}\n{hl*15}{hl*wide*9}')

# 表本体
for i in range(1, 10):
    print(f'{i}{row_head}', end='')
    for j in range(1, 10):
        print(line_up(i*j), end='')
    print()

print()


# 先生の解答例
# 九九表
# for i in range(1, 10):
#     for j in range(1, 10):
#         ans = i * j
#         print(ans, end=" ") if ans > 9 else print(" ", ans, end=" ",sep='')
#     print()
# print()

# ピラミッド(step:段数)
step:int = 20
ast:str = '*'
sp:str = ' '
for i in range(1, step + 1):
    print(f'{sp * (step - i)}{ast * i}') if i == 1 else print(f'{sp * (step - i)}{ast * (2 * i - 1)}')


# continueとbreak
count = 0
l = []
while True:
    count += 1
    hit:int = random.randint(1, 10)
    l.append(hit)
    print(hit)
    if hit == 4:
        print(l)
        avrg = sum(l) / float(len(l))
        print(f'{count}回目に{hit}が出ました')
        print(f'平均値は{avrg}です')
        break
    else:        
        continue