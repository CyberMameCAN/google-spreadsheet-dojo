# Python + gspread + Docker

Dockerコンテナ、Pythonとgspreadでグーグルのスプレッドシートを読み書きするまでのサンプル

## 動かし方

### env

    mv env_sample .env

### コンテナ起動

    docker compose up -d --build

### コンテナの中に入らずに実行

    docker container exec -it project-google-spreadsheet python3 opt/main.py

## 参考

- [gspreadライブラリの使い方まとめ！Pythonでスプレッドシートを操作する](https://tanuhack.com/library-gspread/)
- [Googleスプレッドシートからデータを取得してみよう【Google Sheets API】](https://news.mynavi.jp/techplus/article/excelvbaweb-14/)
- [Pythonでgspreadを使ってspreadsheetのシートへの書き込みと削除する方法！Python初心者の勉強](https://programmer-life.work/python/gspread-write-spreadsheet)

