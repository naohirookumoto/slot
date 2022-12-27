import random
import sys
import datetime
from datetime import datetime

def main(arg):
    # print(f'mainのarg:{arg}')
    if arg == 1:
        janken()
    elif arg == 2:
        hallowWorld()
    elif arg == 3:
        cal()
    elif arg == 4:
        lifetime()
# 1
def janken():
    data = ['グー', 'チョキ', 'パー']
    data_chois = random.choice(data)
    print(f'\n来週のサザエさんは、じゃんけん【 {data_chois} 】！！！\n')

# 2
def hallowWorld():
    print('\n Hello World!! \n')

# 3
def cal():
    num01 = 6.5
    num02 = 2.0
    name = 引数
    print(f'num01:{num01}')
    print(f'num02:{num02}')
    print(f'num01 // num02 : {num01 // num02}')

    print(f'こんにちは{name}さん！　文字列{変数名２}')

    print('単項演算子')
    print('"+"や"-"など')

    print('論理演算子')
    print('and, or, ')
    if not (True and False):
        print("True")
# 4 
def lifetime():
    bd = datetime.date(1980, 5, 21)
    g = datetime.date(2032, 5, 21)
    now = datetime.datetime.now()
    tarmA = g - bd
    print(now, tarmA)
    # tarmB = g - now
    print(f'生まれてから{g}までの期間は{tarmA.days//365}年{tarmA.days%365}日')
    # print(f'現在から{g}までの期間は{tarmB}')
    y = datetime.now().year
    print(f'y:{y}')

if __name__ == '__main__':
    input_list = sys.argv[1:]
    print(f'引数:{input_list}')
    if len(input_list) >= 1:
        if input_list[0].isdigit():
            arg = int(input_list[0])
            # print(f'引数:{input_list}')
            # print(f'type(arg):{type(arg)}')
            # print(f'arg:{arg}')
            main(arg)
        else:
            print('引数を１つ数字で入力してください')
    else:
        print('引数を１つ数字で入力してください')