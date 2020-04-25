import requests,os

def set_message(value):
  return {"message": value}

def set_image(image_name):
  image = image_name + ".png"
  payload = {"message": "\nメッセージ＋画像\n" + image_name + "の画像です"}
  files = {"imageFile": open(image,"rb")}

def message(api,headers,payload):
  requests.post(api,headers = headers,data = payload)

def message_and_image(api,headers,payload,files):
  requests.post(api,headers = headers,data = payload,files = files)

# apiの設定
api = "https://notify-api.line.me/api/notify"
# 送る人間の設定
token = "naK0YLzsQHyzaVjNzFdVmS9CnuA4hoxvW6THqCHlTIh"
headers = {"Authorization": "Bearer " + token} 

#画像の設定

# 実行
# メッセージのみ

message(api,headers,set_message("メッセージのみ"))

# メッセージと画像
# os.chdir("Desktop\VScode\python")
# set_image("スクリーンショット (77)")
# message_and_image(api,headers,payload,files)