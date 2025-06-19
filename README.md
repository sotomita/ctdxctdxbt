# ctdxctdxbt

X-CTDのデータをcsvファイルに変換する

## Requirement
- Python
- Pandas

## Usage

### 1. データ準備
観測ソフトウェアの全データ出力(```*_all.csv```)を取り込む。
(例)```./data/input```ディレクトリにアーカイブする  

### 2. 野帳
野帳のデータを```field_book.csv```に置く。
(例)```./data/field_book.csv```
|列名|説明|
|:---|:---|
|obskey|観測点名|
|filename|観測ファイル|  

(例)  
```
obskey,filename
St1,XCTD-0S111234567890_all.CTD
```
  
### 3. ```namelist.py```を設定
```namelist.py```を編集する。
| 変数名|説明|
|:---|:---|
|```field_book_path```|```field_book.csv```のファイルパスを設定|
|```input_dir```|入力データのディレクトリを指定|
|```output_dir```|出力データのディレクトリを指定|

(例)
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

field_book_path = "./data/field_book.csv"
input_dir = "./data/input"
output_dir = "./data/output"
```

### 4. ```main.py```を実行
```main.py```を実行すると、出力先データディレクトリに```{データ名}.csv```として出力される。

