# ファイル読み書き
msg = 'モードを指定し実行 >> 読込み：ｒ、書込み：ｗ'
print(msg)
args = input()

if args == 'w':
    with open("input.csv", "a", encoding="utf-8") as f:
        f.write('大津,0,1,2\n')
        f.write('山科,10,12,13\n')
        f.write('京都,20,21,22\n')
        f.write('新大阪,30,31,32\n')

elif args == 'r':
    with open("input.csv", "r", encoding="utf-8") as f:
        # 次の1行取得
        print('readline():')
        print(f.readline())
        f.seek(0)
        # 残りの全行取得（リスト型）
        print('readlines():')
        print(f.readlines())
        f.seek(0)
        # 残りの全行取得（平文）
        print('read():')
        text = f.read()
        print(text)
        f.seek(0)

        lines = text.split('\n')
        print('改行分割')
        print(f'lines:{lines}')

        df = []
        for l in lines:
            df.append(l.split(','))
        print('カンマ分割の2次元リスト')
        print(f'df:{df}')
        print(f'df[0][0]:{df[0][0]}')

    with open("outputFile.csv", "w", encoding="utf-8") as outputFile:
        # 書き込み
        for row in df:
            # print(type(row))
            # print(row)
            if len(row) > 1:
                sum = int(row[1]) + int(row[2]) + int(row[3])
                # print(sum)
                row.append(str(sum))
            outputFile.write(",".join(row) + "\n")
        


else:
    print(msg)