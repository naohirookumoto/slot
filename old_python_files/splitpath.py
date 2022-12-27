from scipy.special import comb

n = 20
r = 19
a = comb(n, r, exact=True)
print(f'{n}C{r}:{a}')

# 三項演算子
int2 = 0
bool1 = True if int2 == 1 else False
print(bool1)

print('OK') if int2 == 1 else print('NG')

# Match関数
int3 = 51
match int3:
    case 1:
        print('1が選ばれました')
    case 2:
        print('2が選ばれました')
    case 3:
        print('3が選ばれました')
    case 4:
        print('4が選ばれました')
    case 5:
        print('5が選ばれました')
    case _:
        print('その他が選ばれました')

t1 = ('name1', 'data1')
t2 = ('name1', 'data1', 'data2')
t_list = [t1, t2]
for t in t_list:
    match t:
        case [name, d]:
            print(f't1が選択されました{t}')
        case [name, d, d2]:
            print(f't2が選択されました{t}')

