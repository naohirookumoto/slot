import sqlite3
import collections
import kame
conn = sqlite3.connect("dbData.db")
data = []
cursor = conn.execute("SELECT random_val FROM data_table")

for row in cursor:
    data.append(int(row[0] * 10))

hist_data = collections.Counter(data)

hist_kame = kame.Kame()
hist_kame.histogram(hist_data)
input()

