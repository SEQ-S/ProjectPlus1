# -*- coding: utf-8 -*-
import logging
import os
logging.basicConfig(level=os.environ['LOGGING'])

import json
import boto3
import collections
import datetime
from sources import asw_s3,slack

##########
# ダブル押下時
def double(event, w_dict):
    try:
        ##########
        # S3からダウンロード
        rtn_dict = asw_s3.get_s3(event, w_dict)

        ##########
        # 時間差異
        # 文字列を時間にしてから差異出力
        w_start_time = datetime.datetime.strptime(rtn_dict['StartTime'], "%Y-%m-%d %H:%M:%S")
        w_end_time = datetime.datetime.strptime(w_dict['W_time'], "%Y-%m-%d %H:%M:%S")
        w_dtimedelta = w_end_time - w_start_time

        # 文字列化
        w_diff_time = str(w_dtimedelta)
        
        ##########
        # 辞書作成
        # 社員No,社員名,出退勤、開始時刻、終了時刻、稼働時間、KEY名
        s3_dict = collections.OrderedDict()
        s3_dict = {
            'No':rtn_dict['No'],
            'Name':rtn_dict['Name'],
            'Status':'OUT',
            'StartTime':rtn_dict['StartTime'],
            'EndTime':w_dict['W_time'],
            'DiffTime':w_diff_time,
            'W_time':w_dict['W_time'],
            'Key_name':rtn_dict['Key_name']
        }
        
        ##########
        # S3にアップロード
        asw_s3.put_s3(event, s3_dict)
        
        ##########
        # slackに通知
        slack.finish(event, s3_dict)
        
    except:
        logging.critical("double.double:ERR")
