import sys
from datetime import datetime, timedelta
import datetime as dt

# 自己紹介
def show_myself():
    # 氏名を入力
    print('氏名を入力してください')
    name = input()
    # 誕生日を入力(年、月、日)
    print('誕生日を入力してください\n入力例：1980/5/21')
    bd_s = input()
    bd_l = bd_s.split('/')
    bd_y = int(bd_l[0])
    bd_m = int(bd_l[1])
    bd_d = int(bd_l[2])
    
    # BDから経過日数
    bd = dt.date(bd_y, bd_m, bd_d)
    now = dt.datetime.now().date()
    print(f'bd:{bd}')
    print(f'type(bd):{type(bd)}')
    print(f'now:{now}')
    print(f'type(now):{type(now)}')
    # now = datetime.datetime.now().date()
    life_days = now - bd
    life_days = int(life_days / timedelta (days=1))
    print(f'type(life_days):{type(life_days)}')
    
    print(f'life_days:{life_days}')
    # life_days = life_days.date()
    # 自己紹介文を入力
    print('自己紹介文を入力してください')
    self_intro = input()

    # 出力結果：
    print(f'\n\n氏名：{name}')
    print(f'{bd_y}年{bd_m}月{bd_d}日生まれで、')
    print(f'生まれてから{life_days}日経ちました。')
    print(f'自己紹介文：\n{self_intro}\n\n')

show_myself()

    # bd_y = int(input())
    # print('誕生日を入力してください\n生まれ月')
    # bd_m = int(input())
    # print('誕生日を入力してください\n生まれ日')
    # bd_d = int(input())