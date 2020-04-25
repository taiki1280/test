import requests

class LINENotifyBot:
    API_URL = "https://notify-api.line.me/api/notify"
    def __init__(self,acces_token):
        self.__headers = {"Autorization": "Bearer" + acces_token}

    def send(
        self,message,
        image=None,sticker_package_id=None,sticker_id=None,
        ):
        payload = {
            "message": message,
            "stickerPackageID": sticker_package_id,
            "stickerID": sticker_id,
        }
        files = {}
        if image != None:
            files = {"imageFile": open(image,"rb")}
        r = reques.post(
            LINENotifyBot.API_URL,
            headers=self.__headers,
            data=payload,
            files=files,
        )

        from line_notify_bot import LINENotifyBot

from line_notify_bot import LINENotifyBot

bot = LINENotifyBot(access_token="naK0YLzsQHyzaVjNzFdVmS9CnuA4hoxvW6THqCHlTIh")

bot.send(
    message="Write Your Message",
    image="test.png",  # png or jpg
    sticker_package_id=1,
    sticker_id=13,
    )