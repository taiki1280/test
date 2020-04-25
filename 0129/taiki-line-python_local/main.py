import reply
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

# flaskのwebフレームワークのクラス(Flask)のインスタンス作成
app = Flask(__name__)

# 環境変数取得(heroku)
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

# CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET', None)
# CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

CHANNEL_SECRET = "12da081af1930455df339441bfc1b780"
CHANNEL_ACCESS_TOKEN = "V4S5rqoTZCelWoVsFy7U6+asgXFmSzaXliMpSKbljLlNHtV428r1CWOtkqR0E7xZZqpwU1la1Tw6/68bpL9xODCjy6s7ltJsrmkFP8xUJ7jJt/LH3407c0zmY0WqRq1MfZEj6UycaTs//0D24MUthwdB04t89/1O/w1cDnyilFU="


line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# サーバーが正常に動作しているかの確認
@app.route("/")
def hello_world():
    return "hello world!"


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def mode_select(event):
    obj = reply.Reply(event)
    obj.mode_select()


if __name__ == "__main__":
    # app.run()

    # heroku
    # port = int(os.getenv("PORT"))
    # app.run(host="0.0.0.0", port=port)

    app.run(port=8000)
