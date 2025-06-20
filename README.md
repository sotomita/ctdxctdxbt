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

### 5. XCTD深度時間断面の作図```time_seq_xctd.py```
- 上記を実行する，ただしデータは```XCTD*_all.CTD```ではなく```XCTD*_10m.CTD```を使う
- ```time_seq_xctd.py```を編集し実行する  
| 変数名|説明|
|:---|:---|
|```fig_dir```|図の保存パスの設定|
|```var```|変数を設定|
|```bottom```|作図深度の下限の設定|
|```cut_top```|データ最表層を取り除く高さを設定(default:2m)|
|```cut_bottom```|データ最下層を取り除く高さを設定(default:50m)|
|```times```|作図をする時刻の設定|
変な値が入っていなければ```cut_top```,```cut_bottom```はゼロでも良い．```times```は広めに取っても構わない．


