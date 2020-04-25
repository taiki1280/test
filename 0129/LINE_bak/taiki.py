from linebot.models import MessageEvent, TextMessage, TextSendMessage
from main import line_bot_api
 
# モード選択用初期値
mode = ""
# 電卓モード
# 切り替え初期値(これが無いと作れない)
num_set = False
# カウンター
i = 1
# reply処理(送りたい文字列)

def mode_select(event):
    def reply(*args):
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=v) for v in args]
        )
  # modeをグローバル変数に
    global mode
    # (オウムモードのメソッドでもある。)
    def parrot(value):
        reply(value)

    mode_list = ""
    mode_array = ["コマンド", "オウムモード", "電卓モード"]
    for index in range(1, len(mode_array)):
        if index <= 9:
            head = "0" + str(index)
        else:
            head = str(index)
        mode_list += head + ". " + mode_array[index] + "\n"
    value = event.message.text
    if value == "Command":
        reply("[コマンド一覧]\n現在のコマンドは、\n" + mode_list + "の" + str(len(mode_array) - 1) + "個です。\n番号は書かずに日本語を入力してください。")
    # モード選択
    if value in mode_array and value != "コマンド":
        if mode == "":
            mode = value
            text = mode + "が選択されました。\n[" + mode + "終了]と言われるまで" + mode + "になります。"
            if mode == mode_array[2]:
                global ans_before,num_set
                ans_before = 0
                num_set = False
                text += "\n最初に演算したい数字を入力してください"
            reply(text)
        elif value == mode:
            reply("今" + mode + "やで...？")
        else:
            reply("現在" + mode + "です。\n[" + mode + "終了]と言われるまで" + mode + "になります。\n他のモードに切り替えたい場合は現在のモードを終了してください。")

    if mode != "" and value == mode + "終了":
        reply(mode + "を終了します。")
        mode = ""
    # オウムモード
    if mode == mode_array[1]:
        parrot(value)
    # 電卓モード
    elif mode == mode_array[2]:
        global i,num,op
        if num_set == False:
            if value.isdigit() == True:
                num = value
                num_set = True
                i = 1
                reply("演算子をひらがな(たす,ひく,かける,わる,あまり)で入力してください")
            else:
                if i == 1:
                    reply("それは数字ではありません。\n数字を入力してください")
                elif i == 2:
                    reply("...それも数字じゃないよ？？\n数字を入力してね！")
                elif i <= 5:
                    reply("ん～数字じゃないなぁ...\n数字にしようか？？")
                elif i <= 8:
                    reply("ん～数字って分かる？？？\n１とか２とか小学校で習わなかった？？")
                elif i < 20:
                    reply("いい加減にしろw\n数字入れろって言ってるやんかww")
                else:
                    reply("疲れたので" + mode + "を終了します。\n(つ∀-)ｵﾔｽﾐｰ")
                    mode = ""
                    i = 1
                i += 1
        else :
            # 演算記号の処理
            if value in ["たす", "ひく", "かける", "わる", "あまり"]:
                if value == "たす":
                    op = "+"
                elif value == "ひく":
                    op = "-"
                elif value == "かける":
                    op = "*"
                elif value == "わる" and num != "0":
                    op = "/"
                elif value == "あまり":
                    op = "%"
                else:
                    reply("0による除算は数学上不可能です。","別の演算子を入力してください")
                i = 1

                # 電卓モードの処理
                def calc(v1 ,op):
                    global ans_before
                    ans_after = eval(str(ans_before) + op + v1)
                    answer = (str(v1) + " " + str(op) + " " + str(ans_before) + " = " + str(ans_after))
                    ans_before = ans_after
                    return answer

                reply("演算します\n" + calc(num,op) + "\n次に続けて演算したい数字を入力してください")
                num_set = False
            else:
                if i == 1:
                    reply("それは指定した演算子ではありません。\n指定した演算子を入力してください")
                elif i == 2:
                    reply("...それも指定した演算子じゃないよ？？\n指定した演算子を入力してね！")
                elif i <= 5:
                    reply("ん～指定した演算子じゃないなぁ...\n指定した演算子にしようか？？")
                elif i <= 8:
                    reply("ん～指定した演算子って分かる？？？\n１とか２とか小学校で習わなかった？？")
                elif i < 20:
                    reply("いい加減にしろw\n指定した演算子入れろって言ってるやんかww")
                else:
                    reply("疲れたので" + mode + "を終了します。","(つ∀-)ｵﾔｽﾐｰ")
                    mode = ""
                    i = 1
                i += 1
    else:
        if value == "コマンド":
            reply("[コマンド一覧]\n現在のコマンドは、\n01. オウムモード\n02. 電卓モード\nです。番号は書かずに日本語を入力してください。")
        type = event.source.type
        if type == "user":
            reply(str(event.source.user_id),"個チャやな")
        elif type == "group":
            reply(str(event.source.group_id) + "グループチャット")
        elif type == "room":
            reply(str(event.source.room_id))
        else:
            reply(str(type))