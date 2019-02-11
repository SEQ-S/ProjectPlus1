# -*- coding: utf-8 -*-
import json
import boto3
import collections
from sources import asw_s3,slack

##########
# シングル押下時
def single(w_dict):
    try:
        ##########
        # 辞書作成
        # 社員No,社員名,出退勤、開始時刻、終了時刻、稼働時間、KEY名
        s3_dict = collections.OrderedDict()
        s3_dict = {
            'No':w_dict['No'],
            'Name':w_dict['Name'],
            'Status':'IN',
            'StartTime':w_dict['W_time'],
            'EndTime':'-',
            'DiffTime':'-',
            'W_time':w_dict['W_time'],
            'Key_name':w_dict['Key_name']
        }
        ##########
        # S3にアップロード
        asw_s3.put_s3(s3_dict)
        
        ##########
        # slackに通知
        slack.begin(s3_dict)
    except:
        print("*** single:ERR ***")
