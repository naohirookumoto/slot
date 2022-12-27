#!/usr/bin/env python
import random
import cgitb
import io
import sys
# http://localhost:8000/cgi-bin/fortune.py
cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

html_body = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
<!--    <meta charset="shift-jis">  -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>今日の運勢</title>
</head>
<body>
    今日のあなたの運勢は{}です。
</body>
</html>'''

todays_fortune = random.choice(['大吉', '中吉', '吉', '末吉', '凶', '大凶'])
print('Content-type: text/html')
print('')
print(html_body.format(todays_fortune))
