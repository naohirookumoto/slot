# メンバーCSV出力
import glob
from os import path

while True:
    filepath = path.join(".", "csv", "*.csv") # 文字列：'./csv/*.csv'
    files = glob.glob(filepath) # files = ['./csv/1.csv', './csv/2.csv', './csv/3.csv', './csv/4.csv']
    print('\n既存ファイルを編集する場合は【ファイル番号の数字】を入力してください')
    print('新規作成する場合は【 n 】を入力してください')
    print('終了する場合は【 q 】を入力してください')
    print('\n出力ディレクトリ内のCSVファイルを表示します')
    csv_file_l = []
    for i, file_t in enumerate(files): # [0番インデックス, './csv/2.csv', './csv/3.csv', './csv/4.csv']
        print(f'csvファイル番号：{i}、ファイル名：{file_t}')
        csv_file_l.append(file_t) # csv_file_l
    args:str = input()

    # 終了
    if args == 'q':
        print('終了します')
        break

    # 新規作成モード
    elif args == 'n':
        print('ファイル名を入力してください')
        f_new_name:str = input()
        f_pass = path.join(".", "csv", f"{f_new_name}.csv")
        # 新規作成のファイル名が既存と同じ場合
        for i, file in enumerate(files):
            if file == f_pass:
                print(f'入力されたファイル名は既に存在します。')

        with open(f_pass, "w+", encoding="utf-8") as f:
            print('追加する氏名をカンマ区切りで入力してください')
            men = input()
            men_l = men.split(',')
            f.write(",".join(men_l))

    # 既存ファイル選択
    else:
        if len(csv_file_l) >= int(args):
            f_name = csv_file_l[int(args)]
            print(f'選択したファイル{f_name}を表示します')
            df = []
            with open(f_name, "r", encoding="utf-8") as f:
                f.seek(0)
                text_l = f.readlines()
                for text in text_l:
                    staff = text.split(',')
                    for s in staff:
                        df.append(s)
                print(f'{df}')
                
            print('選択するモードの数字を入力してください\n １：追記モード\n ２：既存データ削除しデータ入力モード\n q：終了\n')
            mode:str = input()
            print('カンマ区切りで追加する氏名を入力してください')
            men:str = input()
            df_add:list = men.split(',')

            # 追記モード
            if mode == 'q':
                break
            elif mode == '1':
                pass
            # 初期化して追記モード
            elif mode == '2':
                df = []
            else:
                print('不正な値が入力されたため強制終了します')
                break

            for new_man in df_add:
                # print(f'new_man:{new_man}')
                df.append(new_man)

            with open(f_name, "+w", encoding="utf-8") as f:
                f.write(",".join(df))
                print(f'処理結果を表示\n{f.readline}')

        else:
            print(f'ファイル番号：{args} は存在しません')

# ファイル書き込みから結果表示
def makefile(filepass:str, l:list):
    f.seek(0)
    # 書き込み
    with open(filepass, "+w", encoding="utf-8") as f:
        f.write(",".join(l))
    # 表示
    df = []
    with open(f_name, "r", encoding="utf-8") as f:
        f.seek(0)
        text_l = f.readlines()
        for text in text_l:
            staff = text.split(',')
            for s in staff:
                df.append(s)
        print(f'{df}')
