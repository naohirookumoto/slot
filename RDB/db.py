import sqlite3
import itertools
import random

# DB接続
conn = sqlite3.connect('my_database.db')
# テーブル作成
# sql = conn.execute('CREATE TABLE data_table(id INTEGER, random_val REAL)')
# conn.execute(sql)
# データ入力
iteratorCount = itertools.count(1)
for i in range(500):
    rnd = random.random()
    insert_sql = "INSERT INTO data_table VALUES({}, {})".format(next(iteratorCount), rnd)
    conn.execute(insert_sql)
conn.commit()

# データ削除
delete_sql = "DELETE FROM data_table WHERE id = 1"
# conn.execute(delete_sql)
# conn.commit()

# データ抽出
select_sql = "SELECT id, random_val FROM data_table"
cursor = conn.execute(select_sql)

# 検索結果の表示
for data in cursor:
    print(f'data:{data}')

print(f'len(cursor):{len(list(cursor))}')
print(cursor)


