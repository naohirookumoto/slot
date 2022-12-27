import random

men:list = ['宇賀','奥本','片山','川島','小林','白濵','高橋','中島','中谷','藤田']
guide:str = ('\n1, 2, q のいずれかを入力してください\
    \n 1: 1名の名前が指定されます\
    \n 2: 10名の名前が順番がランダムに表示されます\
    \n q: プログラムを終了します。\n')

while True:
    print(guide)
    args:str = input()
    random.shuffle(men)

    if args == '1':
        msg = f'【 {men[0]} 】\n'
    elif args == '2':
        msg = f'{men}\n'
    elif args == 'q':
        break
    else:
        msg = guide

    print(msg)