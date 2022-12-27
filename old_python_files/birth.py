import random
import sys
import datetime
# from datetime import datetime
# 引数に生年月日
input_list = sys.argv[1:]
print(input_list)
year = int(input_list[0])
month = int(input_list[1])
day = int(input_list[2])
print(year, month, day)

# 誕生日からの年数と日数
def lifetime(year, month, day):
    print('誕生日からの経過日数を知りたい年を入力')
    now_y = int(input())
    print('誕生日からの経過日数を知りたい月を入力')
    now_m = int(input())
    print('誕生日からの経過日数を知りたい日を入力')
    now_d = int(input())
    print(now_y, now_m, now_d)

    bd = datetime.date(year, month, day)
    g = datetime.date(now_y, now_m, now_d)
    now = datetime.datetime.now()
    tarmA = g - bd
    print(now, tarmA)
    # tarmB = g - now
    print(f'生まれてから{g}までの期間は{tarmA.days//365}年{tarmA.days%365}日')
    # print(f'現在から{g}までの期間は{tarmB}')


lifetime(year, month, day)