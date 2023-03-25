import requests
from os import environ, system, path
from sys import exit

'''
cron: 30 15 * * *
new Env('阿里云盘签到');
APP抓包refresh_token
token有效期未知，报错就换token
变量:ali_ck   多账号#号隔开

浏览器打开 阿里云盘 aliyundrive.com
登陆后
使用快捷键 Ctrl + Shift + C edge浏览器或者google chrome 打开开发者控制台，选择 Console（控制台）粘贴下面的代码

alert(JSON.parse(localStorage.token).refresh_token)

'''

def load_send():
    global send, mg
    cur_path = path.abspath(path.dirname(__file__))
    if path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
            print("加载通知服务成功！")
        except:
            send = False
            print("加载通知服务失败~")
    else:
        send = False
        print("加载通知服务失败~")


load_send()


class AliDrive_CheckIn:
    def __init__(self, refresh_token):
        self.userAgent = "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 D/C501C6D2-FAF6-4DA8-B65B-7B8B392901EB"
        self.aliYunPanToken = ''
        self.aliYunPanRefreshToken = ''
        self.refresh_token = refresh_token
        self.msg = ''
        self.user_name = ''

    def getToken(self):
        url = 'https://auth.aliyundrive.com/v2/account/token'
        headers = {
            "Content-Type": "application/json; charset=utf-8",
        }
        body = {
            "grant_type": "refresh_token",
            "app_id": "pJZInNHN2dZWk8qg",
            "refresh_token": self.refresh_token
        }
        response = requests.post(url, headers=headers, json=body)
        try:
            resp = response.json()
            # print(resp)
            if 'InvalidParameter.RefreshToken' in resp:
                # print('RefreshToken 有误请检查！')
                self.msg += 'RefreshToken 有误请检查！'
                exit(0)
            else:
                self.aliYunPanToken = f'Bearer {resp["access_token"]}'
                self.aliYunPanRefreshToken = resp["refresh_token"]
                self.user_name = resp["user_name"]

                # print(self.aliYunPanToken)
                # print(self.aliYunPanRefreshToken)
                # print("获取token成功，开始执行签到！")
                self.msg += f"账号：【{self.user_name}】\n获取token成功，开始执行签到！\n"
                self.CheckIn()
        except:
            print(response.text())

    def CheckIn(self):
        sign_url = 'https://member.aliyundrive.com/v1/activity/sign_in_list'
        sign_headers = {
            "Content-Type": "application/json",
            "Authorization": self.aliYunPanToken,
            "User-Agent": self.userAgent
        }
        sign_body = {}
        sign_res = requests.post(sign_url, headers=sign_headers, json=sign_body)
        try:
            sign_resp = sign_res.json()
            # print(sign_resp)
            result = sign_resp['result']
            signInCount = result['signInCount']
            isReward = result['isReward']
            if isReward == True:
                # print(f'签到成功！已累计签到{signInCount}天！')
                self.msg += f'签到成功！已累计签到{signInCount}天！\n'
            else:
                # print(f'今日已签到！已累计签到{signInCount}天！')
                self.msg += f'今日已签到！已累计签到{signInCount}天！\n'
            signInLogs = sign_resp['result']['signInLogs']
            for l in signInLogs:
                if l['status'] != 'miss':
                    # print(f'第{l["day"]}天，获得{l["notice"]}')
                    self.msg += f'第{l["day"]}天，获得{l["notice"]}\n'
            send('阿里云盘签到通知', self.msg)
        except:
            # print(sign_res)
            self.msg += sign_res


if __name__ == '__main__':
    refresh_token = ''
    ali_ck = environ.get("ali_ck") if environ.get("ali_ck") else refresh_token
    if ali_ck == "":
        print("未填写refresh_token 青龙可在环境变量设置 ali_ck 或者在本脚本文件上方将获取到的refresh_token填入cookie中")
        exit(0)
    for ck in ali_ck.split("#"):
        Sign = AliDrive_CheckIn(ck)
        Sign.getToken()
