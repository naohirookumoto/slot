# メンバーCSV出力
import glob
from os import path

# ファイル書き込みから結果表示する関数
def makefile(filepass:str, d:list, mode:str):
    # 書込みモード
    if mode == '+w':
        with open(filepass, mode, encoding="utf-8") as f:
            f.seek(0)
            f.write(",".join(d))
    # 読込表示モード
    elif mode == 'r':
        showList:list = []
        with open(filepass, mode, encoding="utf-8") as f:
            f.seek(0)
            text_l = f.readlines()
            for text in text_l:
                staff = text.split(',')
                for s in staff:
                    showList.append(s)
            print(f'ファイル内容を表示\n{showList}')
        return showList
    else:
        print('不正なモードが選択されました')

# qが入力されるまで繰り返し
while True:
    # CSVファイル置き場のパスをワイルドカードで準備
    filepath:str = path.join(".", "csv", "*.csv")
    # 各CSVファイルパスが要素のリストを作成
    files:list = glob.glob(filepath)
    csv_file_l:list = []
    print('\n出力ディレクトリ内のCSVファイルを表示します')
    # CSVディレクトリ内のCSVファイルを一覧表示
    for i, file_t in enumerate(files):
        print(f'ファイル番号：{i}、ファイルパス：{file_t}')
        csv_file_l.append(file_t)

    print('\n既存ファイルを編集する場合は【ファイル番号の数字】を入力してください')
    print('新規作成する場合は【 n 】を入力してください')
    print('終了する場合は【 q 】を入力してください')

    # 終了の q か、新規の n 、既存のファイル番号の数字の何れかが入力される想定
    args:str = input()

    # 終了
    if args == 'q':
        print('終了します')
        break

    # 新規作成モード
    elif args == 'n':
        print('ファイル名を入力してください')
        f_new_name:str = input()
        # 入力されたファイル名のファイルパスを作成
        f_pass:str = path.join(".", "csv", f"{f_new_name}.csv")
        # 新規作成のファイル名が既存と同じ場合
        for i, file in enumerate(files):
            if file == f_pass:
                print(f'入力されたファイル名は既に存在します。別のファイル名か、既存ファイル番号を入力してください')
                break
        print('追加する氏名をカンマ区切りで入力してください')
        men:str = input()
        men_l:list = men.split(',')
        # 新規CSVファイル作成
        makefile(f_pass, men_l, '+w')
        # ファイル内容を表示
        makefile(f_pass, men_l, 'r')

    # 既存ファイル選択
    else:
        if not args:
            print('不適切な引数が入力されました。終了します')
            break
        # リスト要素にアクセスする際Out of bounce error対策
        if len(csv_file_l) >= int(args):
            # インデックス番号を指定して１つのCSVファイルを指定
            f_name:str = csv_file_l[int(args)]
            print(f'選択したファイル{f_name}を表示します')
            # 処理の最後にCSVへ書き込むリストを初期化（このリストを育てる）
            df:list = []
            # ファイルの内容を表示し既存データを取得
            df = makefile(f_name, df, 'r')
                
            print('選択するモードの数字を入力してください\n 1：追記モード\n 2：既存データ削除しデータ入力モード\n q：終了\n')
            mode:str = input()
            # 終了
            if mode == 'q':
                print('処理を終了します')
                break
            # 追記モード
            elif mode == '1':
                pass
            # 初期化して追記モード
            elif mode == '2':
                # 既存データを初期化
                df = []
            else:
                print('不正な値が入力されたため強制終了します')
                break

            print('カンマ区切りで追加する氏名を入力してください')
            men:str = input()
            df_add:list = men.split(',')
            for new_man in df_add:
                # 既存データに新しく入力されたデーアを追加
                df.append(new_man)
            # ファイルへ書込み
            makefile(f_name, df, '+w')
            # ファイル内容を表示
            makefile(f_name, df, 'r')

        else:
            print(f'ファイル番号：{args} は存在しません\n処理を終了します')
            break
