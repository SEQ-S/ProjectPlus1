# -*- coding: utf-8 -*-
import json
import os
import requests
from slackweb import slackweb

##########
# 変数定義
SLACK_URL=os.environ['SLACK_URL']
SLACK_TOKEN=os.environ['SLACK_TOKEN']
SLACK_CHANNEL=os.environ['SLACK_CHANNEL']

##########
# 出勤時
def begin(w_dict):
    try:
        ##########
        # メッセージ出力先設定
        slack = slackweb.Slack(url=SLACK_URL)
        
        ##########
        # メッセージ出力形式
        attachment_list = []
        attachment = {
            "pretext":"勤怠管理連絡 -出勤-",
            "text":"勤怠管理連絡 -出勤-",
            # lime
            "color":"#00ff00",
            "fields":[
                {
                    "title":"社員番号",
                    "value":w_dict['No'],
                    "short": "true"
                },
                {
                    "title":"社員名",
                    "value":w_dict['Name'],
                    "short": "true"
                },
                {
                    "title":"出勤時間",
                    "value":w_dict['StartTime'],
                    "short": "true"
                },
                {
                    "title":"退勤時間",
                    "value":"-",
                    "short": "true"
                },
                {
                    "title":"稼働時間",
                    "value":"-",
                    "short": "true"
                }
            ]
        }
        
        ##########
        # メッセージを送信
        attachment_list.append(attachment)
        slack.notify(attachments=attachment_list)
    except:
        print("*** begin:ERR ***")



##########
# 退勤時時
def finish(w_dict):
    try:
        ##########
        # メッセージ出力先設定
        slack = slackweb.Slack(url=SLACK_URL)
        
        ##########
        # メッセージ出力形式
        attachment_list = []
        attachment = {
            "pretext":"勤怠管理連絡 -退勤-",
            "text":"勤怠管理連絡 -退勤-",
            # darkblue
            "color":"#00008b",
            "fields":[
                {
                    "title":"社員番号",
                    "value":w_dict['No'],
                    "short": "true"
                },
                {
                    "title":"社員名",
                    "value":w_dict['Name'],
                    "short": "true"
                },
                {
                    "title":"出勤時間",
                    "value":w_dict['StartTime'],
                    "short": "true"
                },
                {
                    "title":"退勤時間",
                    "value":w_dict['EndTime'],
                    "short": "true"
                },
                {
                    "title":"稼働時間",
                    "value":w_dict['DiffTime'],
                    "short": "true"
                }
            ]
        }
        
        ##########
        # メッセージを送信
        attachment_list.append(attachment)
        slack.notify(attachments=attachment_list)
    except:
        print("*** finish:ERR ***")
        

##########
# ファイルアップロード時
def upload_file(w_dict):
    try:
        ##########
        # 情報整理
        files = {'file': open("/tmp/pandas.csv", 'r')}
        param = {
            'token':SLACK_TOKEN,
            'channels':SLACK_CHANNEL,
            'filename':w_dict['No'] + w_dict['Name'] + ".csv",
            'initial_comment': w_dict['No'] + w_dict['Name'] ,
            'title': w_dict['No'] + w_dict['Name']
        }
        
        ##########
        # ファイルアップ
        requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
        
        ##########
        # ファイルをオープンする
        test_data = open("/tmp/pandas.csv", "r")
        # 一行ずつ読み込んでは表示する
        for line in test_data:
            print(line)
        # ファイルをクローズする
        test_data.close()

    except:
        print("*** upload_file:ERR ***")
