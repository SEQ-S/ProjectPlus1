# -*- coding: utf-8 -*-
import logging
import os
logging.basicConfig(level=os.environ['LOGGING'])

import time
import datetime
import pytz
import json
import sys
import collections
from sources import single, double, long

##########
# 処理開始
def lambda_handler(event, context):
    try:
        ##########
        # 変数定義
        w_employee_no = event['placementInfo']['attributes']['EMPLOYEE_NO']
        w_employee_name = event['placementInfo']['attributes']['EMPLOYEE_NAME']

        ##########
        # 時間設定
        w_localtime = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        w_time = w_localtime.strftime("%Y-%m-%d %H:%M:%S")
        w_key = w_localtime.strftime("%Y%m%d%H%M%S")

        ##########
        # 辞書作成
        # 社員No,社員名,稼働時間、KEY名
        w_dict = collections.OrderedDict()
        w_dict = {
            'No':w_employee_no,
            'Name':w_employee_name,
            'W_time':w_time,
            'Key_name':w_key
        }
        
        ##########
        # ボタン振り分け
        divide_clicktype(event,w_dict)
        
        ##########
        # リターン
        return {
            'statusCode': 200,
            'event':json.dumps(event),
            'body': json.dumps("*** lambda_handler:OK ***")
        }
    except:
        logging.critical("lambda_handler:ERR")

##########
# ボタン振り分け
def divide_clicktype(event,w_dict):
    try:
        ##########
        # クリックタイプ取得
        click_type = event['deviceEvent']['buttonClicked']['clickType']

        ##########
        # 振り分け
        if click_type == 'SINGLE':
            single.single(event,w_dict)
        elif click_type == 'DOUBLE':
            double.double(event,w_dict)
        elif click_type == 'LONG':
            long.long(event,w_dict)
    except:
        logging.critical("divide_clicktype:ERR")
