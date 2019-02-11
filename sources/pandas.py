# -*- coding: utf-8 -*-
import sys
import json
import boto3
import pandas as pd

##########
# ロング押下時
def molding(w_list):
    try:
        ##########
        # list型をpandasに読み込み
        df = pd.io.json.json_normalize(w_list)
        
        ##########
        # 不要な列を削除する
        # No,Name,Status,W_time,Key_name
        del df['No']
        del df['Name']
        del df['Status']
        del df['W_time']
        del df['Key_name']
        
        ##########
        # 残ったカラム名変更
        df.rename(columns={'StartTime' : '開始時刻'}, inplace=True)
        df.rename(columns={'EndTime' : '終了時刻'}, inplace=True)
        df.rename(columns={'DiffTime' : '稼働時間'}, inplace=True)
        
        ##########
        # 列を追加する
        # 日付＝値は開始時間と合わせる
        # 型をObject⇨datetime
        df['日付'] = pd.to_datetime(df['開始時刻'])
        # 型をdatetime⇨date
        df['日付'] = df['日付'].dt.date
        
        ##########
        # 列を並び替え
        # 日付、開始時刻、終了時刻、稼働時間
        df = df.ix[:,['日付','開始時刻','終了時刻','稼働時間']]
        
        df = df.set_index(['日付','開始時刻'])
        ##########
        # StartTimeで昇順にソート
        df.sort_values(['日付','開始時刻'], inplace=True)
        
        ##########
        # ファイル出力
        df.to_csv('/tmp/pandas.csv')
        
    except:
        print("*** molding:ERR ***")
