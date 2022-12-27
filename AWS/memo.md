
## 現在のアドレス設定を確認するには以下のコマンドを打ちます。

mysql&gt; select * from wp_options where option_name = 'siteurl';

mysql&gt; select * from wp_options where option_name = 'home';

WordPressアドレスは、WordPressコアファイルが存在するアドレスです。
サイトアドレスは、ユーザーがブラウザに入力してWordPressブログにアクセスするためのアドレスです。
この情報を新しいアドレスに変えてあげれば良いです。

UPDATE wp_options set option_value='https://kunren02.blog.22d100401.tk' where option_name='siteurl';

UPDATE wp_options set option_value='https://kunren02.blog.22d100401.tk' where option_name='home';


RDS(mariaDB)
エンドポイント
wordpressdb-kunren02.ctlhymgblizp.ap-northeast-1.rds.amazonaws.com


## EC2
kunren00-sg
インバウンド
 - http,https.sshポート

アウトバウンド
- Any Ok

kunren00-PRIVATE-sg
インバウンド
 - Any Ok

アウトバウンド
- mysqlのポートでkunren00-private-sgからのアクセスを許可

## RDS
kunren00-RDS-sg
インバウンド
 - mysqlのポートでkunren00-private-sgからのアクセスを許可

アウトバウンド
- Any Ok





EC2で作成したｄｂ名がDB１

RDSを作成した時に指定したDB名がDB２

SQLリストアで指定するDB名は「DB2」を指定しないとだめ

ドメイン名
22d100401.tk
http://ec2-3-113-24-162.ap-northeast-1.compute.amazonaws.com/

https://kunren02.blog.22d100401.tk/

https://kunren02.s3.22d100401.tk/

http://kunren02.s3.22d100401.tk.s3-website-ap-northeast-1.amazonaws.com

WordPressの管理ログイン画面
https://kunren02.blog.22d100401.tk/wp-login.php


