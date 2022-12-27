# 星座を判定し本日の運勢を表示
import requests
import json
import datetime as dt
ARIES = 'おひつじ座'
TAURUS = 'おうし座'
GEMINI = 'ふたご座'
CANCER = 'かに座'
LEO = 'しし座'
VIRGO = 'おとめ座'
LIBRA = 'てんびん座'
SCORPIO = 'さそり座'
SAGITTARIUS = 'いて座'
CAPRICORN = 'やぎ座'
AQUARIUS = 'みずがめ座'
PISCES = 'うお座'

# 生年月日
print('生年月日を入力してください 例:1980/5/21')
bd_l = input().split('/')
bd_y:int = int(bd_l[0])
bd_m:int = int(bd_l[1])
bd_d:int = int(bd_l[2])
bd:dt = dt.datetime(bd_y, bd_m, bd_d, 0 ,0)

# 12星座の日付情報
aries_s:dt = dt.datetime(bd_y, 3, 21)
aries_e:dt = dt.datetime(bd_y, 4, 19)
taurus_s:dt = dt.datetime(bd_y, 4, 20)
taurus_e:dt = dt.datetime(bd_y, 5, 20)
gemini_s:dt = dt.datetime(bd_y, 5, 21)
gemini_e:dt = dt.datetime(bd_y, 6, 21)
cancer_s:dt = dt.datetime(bd_y, 6, 22)
cancer_e:dt = dt.datetime(bd_y, 7, 22)
leo_s:dt = dt.datetime(bd_y, 7, 23)
leo_e:dt = dt.datetime(bd_y, 8, 22)
virgo_s:dt = dt.datetime(bd_y, 8, 23)
virgo_e:dt = dt.datetime(bd_y, 9, 22)
libra_s:dt = dt.datetime(bd_y, 9, 23)
libra_e:dt = dt.datetime(bd_y, 10, 23)
scorpio_s:dt = dt.datetime(bd_y, 10, 24)
scorpio_e:dt = dt.datetime(bd_y, 11, 22)
sagittarius_s:dt = dt.datetime(bd_y, 11, 23)
sagittarius_e:dt = dt.datetime(bd_y, 12, 21)
capricorn_s:dt = dt.datetime(bd_y, 12, 22)
capricorn_e:dt = dt.datetime(bd_y, 1, 19)
aquarius_s:dt = dt.datetime(bd_y, 1, 20)
aquarius_e:dt = dt.datetime(bd_y, 2, 18)
pisces_s:dt = dt.datetime(bd_y, 2, 19)
pisces_e:dt = dt.datetime(bd_y, 3, 20)

if aries_s <= bd <= aries_e:
    my_zpdiac = ARIES
    index:int = 0
elif taurus_s <= bd <= taurus_e:
    my_zpdiac = TAURUS
    index:int = 1
elif gemini_s <= bd <= gemini_e:
    my_zpdiac = GEMINI
    index:int = 2
elif cancer_s <= bd <= cancer_e:
    my_zpdiac = CANCER
    index:int = 3
elif leo_s <= bd <= leo_e:
    my_zpdiac = LEO
    index:int = 4
elif virgo_s <= bd <= virgo_e:
    my_zpdiac = VIRGO
    index:int = 5
elif libra_s <= bd <= libra_e:
    my_zpdiac = LIBRA
    index:int = 6
elif scorpio_s <= bd <= scorpio_e:
    my_zpdiac = SCORPIO
    index:int = 7
elif sagittarius_s <= bd <= sagittarius_e:
    my_zpdiac = SAGITTARIUS
    index:int = 8
elif capricorn_s <= bd <= capricorn_e:
    my_zpdiac = CAPRICORN
    index:int = 9
elif aquarius_s <= bd <= aquarius_e:
    my_zpdiac = AQUARIUS
    index:int = 10
elif pisces_s <= bd <= pisces_e:
    my_zpdiac = PISCES
    index:int = 11

date:dt = dt.datetime.today().strftime("%Y/%m/%d")
# 占いサイト、ジュゲムさんのAPIを利用
# http://api.jugemkey.jp/api/horoscope/year/month/day の形式
res = requests.get(url='http://api.jugemkey.jp/api/horoscope/free/'+ date)

# 全星座表示
# print(json.dumps(json.loads(res.text), indent=4, ensure_ascii=False))

# 入力された生年月日の星座情報のみ取得
today_lucks = res.json()["horoscope"][date][index]
# print(res.json()["horoscope"][date][index]['item'])
sign = today_lucks['sign']
content = today_lucks['content']
item = today_lucks['item']
money = today_lucks['money']
total = today_lucks['total']
job = today_lucks['job']
color = today_lucks['color']
day = today_lucks['day']
love = today_lucks['love']
rank = today_lucks['rank']
msg = (
    f'{bd.year}年{bd.month}月{bd.day}生まれの\
    \n今日のあなたの星座【 {sign} 】の運勢は\
    \n{content}\n幸運のアイテムは{item}\
    \n幸運の色は{color}\n総合の運勢：{total}/5\
    \n仕事運　　：{job}/5\n愛情運　　：{love}/5\
    \n金運　　　：{money}/5\n以上、本日の運勢でした。\
    \nステキな一日でありますように。'
)
print(msg)