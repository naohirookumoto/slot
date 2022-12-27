import datetime

today:datetime = datetime.datetime.now()
youbi:int = today.weekday()
s:str = ''
msg2:str = ''
# youbi = 6
match youbi:
    case 4:
        msg = 'ゆっくりやろー'
    case 5 | 6:
        msg = '休日だー'
    case _:
        msg = '頑張って働こう'

match youbi:
    case 0:
        msg2 = '月'
    case 1:
        msg2 = '火'
    case 2:
        msg2 = '水'
    case 3:
        msg2 = '木'
    case 4:
        msg2 = '金'
    case 5:
        msg2 = '土'
    case 6:
        msg2 = '日'

print(f'{msg2}曜日だ、{msg}')