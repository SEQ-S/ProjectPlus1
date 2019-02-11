# -*- coding: utf-8 -*-
import logging
import os
logging.basicConfig(level=os.environ['LOGGING'])

import json
import boto3
from sources import asw_s3,slack,pandas

##########
# ロング押下時
def long(event, w_dict):
    try:
        ##########
        # S3からダウンロード（全量）
        dict_list = asw_s3.get_s3_all(event, w_dict)
        
        ##########
        # ファイル編集
        pandas.molding(event, dict_list)
        
        ##########
        # slack連携
        slack.upload_file(event, w_dict)

    except:
        logging.critical("long.long:ERR")
