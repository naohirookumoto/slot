# 年齢を1つ入力 判定結果を表示する。
Y_1 = '幼年' # 「幼年」は0～4歳
Y_2 = '少年' # 「少年」は5～14歳
Y_3 = '青年' # 「青年」は15～24歳
M_1 = '壮年' # 「壮年」は25～44歳
M_2 = '中年' # 「中年」は45～64歳
O_1 = '高年' # それ以上は「高年」

AGE_60 = '還暦' # 還暦（かんれき）・・・60歳
AGE_70 = '古希' # 古希（こき）・・・70歳
AGE_77 = '喜寿' # 喜寿（きじゅ）・・・77歳
AGE_80 = '傘寿' # 傘寿（さんじゅ）・・・80歳
AGE_88 = '米寿' # 米寿（べいじゅ）・・・88歳
AGE_90 = '卒寿' # 卒寿（そつじゅ）・・・90歳
AGE_99 = '白寿' # 白寿（はくじゅ）・・・99歳
AGE_100 = '百寿' # 百寿（ももじゅ） ・・・100歳
AGE_108 = '茶寿' # 茶寿（ちゃじゅ）・・・108歳
AGE_111 = '皇寿' # 皇寿（こうじゅ）・・・111歳
AGE_120 = '大還暦' # 大還暦（だいかんれき）・・・120歳
AGE_250 = '天寿' # 天寿（てんじゅ）・・・250歳
CONCAT = 'で'

age:int = int(input())
s1:str = ''
s2:str = ''

if age <= 4:
    s1 = Y_1
elif age < 14:
    s1 = Y_2
elif age < 24:
    s1 = Y_3
elif age < 44:
    s1 = M_1
elif age < 64:
    s1 = M_2
else:
    s1 = O_1

if age == 60:
    s2 = AGE_60
elif age == 70:
    s2 = AGE_70
elif age == 77:
    s2 = AGE_77
elif age == 80:
    s2 = AGE_80
elif age == 88:
    s2 = AGE_88
elif age == 90:
    s2 = AGE_90
elif age == 99:
    s2 = AGE_99
elif age == 100:
    s2 = AGE_108
elif age == 111:
    s2 = AGE_111
elif age == 120:
    s2 = AGE_120
elif age == 250:
    s2 = AGE_250

if len(s2) > 0:
    s2 = f'{CONCAT}{s2}'
print(f'{s1}{s2}')


print(f's1:{s1}')
print(f's2:{s2}')

