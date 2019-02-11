# -*- coding: utf-8 -*-
import json
import boto3
from sources import asw_s3,slack,pandas

##########
# ロング押下時
def long(w_dict):
    try:
        ##########
        # S3からダウンロード（全量）
        dict_list = asw_s3.get_s3_all(w_dict)
        
        ##########
        # ファイル編集
        pandas.molding(dict_list)
        
        ##########
        # slack連携
        slack.upload_file(w_dict)

    except:
        print("*** long:ERR ***")
