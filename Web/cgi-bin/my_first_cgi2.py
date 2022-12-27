#!/usr/bin/env python

html_body = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Page</title>
</head>
<body>
    初めてのCGI
</body>
</html>'''

print('Content-type: text/html')
print('')
print(html_body)
input()