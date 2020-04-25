import sys
from linebot.models import TextSendMessage
from main import line_bot_api
import random



""" イベントハンドラー(メッセージを受け取ったとき)が実行される前に初期化しておかないと動作不可能な変数 """
# モード選択用
RUNNING_ID_DICT = {}


class Reply:
    # モードの初期化
    MODE_ARRAY = ["コマンド", "管理者モード", "command", "こまんど", "オウムモード",
                  "電卓モード", "計算モード", "沈黙モード", "財布モード", "相談モード", "特定の言葉モード","サイコロモード"]
    SAD_WORD_ARRAY = ["死ね", "しね", "消えろ", "きえろ", "カス",
                      "かす", "クズ", "くず", "ゴミ", "ごみ", "ポンコツ", "ぽんこつ"]

    def __init__(self, event):
            # 引数として受け取ったeventをself.event変数に代入
        self.event = event
            # 受け取った場所(個チャ,グルチャ,ルームチャ)をself.type変数に代入
        self.type = event.source.type
            # 受け取った文字をtext変数へ
        self.text = event.message.text
            # botが使われている場所を一意に特定し、特定したIDの名前で、辞書を作成する
        if self.type == "user":
            self.RUNNING_ID = self.event.source.user_id
        elif self.type == "room":
            self.RUNNING_ID = self.event.source.room_id
        elif self.type == "group":
            self.RUNNING_ID = self.event.source.group_id

        # モード選択メソッド
    def mode_select(self):
        RUNNING_ID_DICT.setdefault(self.RUNNING_ID, {"モード": "デフォルトモード"})
        """ モードに関わらず条件によって実行される処理 """
        # user,room,groupのいづれかのidによって初期値を設定
        self.MODE = RUNNING_ID_DICT[self.RUNNING_ID]["モード"]
        if self.text in ["Command", "command"]:
            self.command()
        if self.text in ["@bye", "退会願います", "帰れ", "去れ"]:
            RUNNING_ID_DICT.pop(self.RUNNING_ID)
            self.leave()
        # モード変更メソッド
        elif self.MODE == "デフォルトモード":
            import default_mode
            default_mode.run(self)
            # self.default_mode()
            """ 各モードによってすることを変更する """
        else:
            # モード選択済みの時
            if self.text == self.MODE + "終了":
                self.mode_fin()
            elif self.MODE == "管理者モード":
                self.admin_mode()
            elif self.MODE == "オウムモード":
                self.parrot_mode()
            elif self.MODE == "沈黙モード":
                pass
            elif self.MODE == "電卓モード":
                import calc_mode
                calc_mode.run(self)
            elif self.MODE == "計算モード":
                import calculation_mode
                calculation_mode.run(self)
            elif self.MODE == "相談モード":
                import consultation_mode
                consultation_mode.run(self)
            elif self.MODE == "特定の言葉モード":
                import specific_words_mode
                specific_words_mode.run(self)
            elif self.MODE == "サイコロモード":
                import dice_mode
                dice_mode.run(self)
            # 理論上ありえないと思うが念の為。
            else:
                self.reply("何のモードか分からん" + self.MODE)

    def leave(self):
        # グループ又はルームチャットの時
        if self.type in ["room", "group"]:
            if self.MODE == "デフォルトモード":
                self.reply("分かりました。")
                if self.type == "group":
                    line_bot_api.leave_group(self.event.source.group_id)
                else:
                    line_bot_api.leave_room(self.event.source.room_id)
            else:
                self.reply("現在" + self.MODE + "です。",
                           "退会させるためには、" + self.MODE + "を終了してください。")

        # コマンドメソッド(コマンド一覧作成メソッド)
    def command(self):
        self.reply("現在使用可能なコマンドは" + str(len(self.MODE_ARRAY) - 1) + "個です。",
                   "「コマンド一覧」\n" + self.modelist(), "日本語のみを入力してください。", "例）オウムモード")

    def hira_command(self):
        self.reply("[ひらがなこまんどいちらん]\n(これはてにゅうりょくです)\nげんざいのこまんどは、\nいち、 おうむもーど\nにぃ、 でんたくもーど\nさん、 ちんもくもーど\nです。",
                   "ばんごうはかかずににほんごをにゅうりょくしてぷりーず。")

    def modelist(self):
        mode_list = ""
        for index in range(1, len(self.MODE_ARRAY)):
            if index <= 9:
                head = "0" + str(index)
            else:
                head = str(index)
            mode_list += "\n" + head + ". " + self.MODE_ARRAY[index]
        return mode_list


        # 管理者モード
    def admin_mode(self):
        if self.text == "Userid":
            self.reply("ユーザーID", str(self.event.source.user_id))
            """ メッセージをしてきた人間によって処理 """
            # 大樹の場合
        if self.event.source.user_id == "Uffc2e609077732c505aae085ba524938":
            # グループの場合
            if self.text == "Groupid":
                if self.type == "group":
                    self.reply("グループID", str(self.event.source.group_id))
                else:
                    self.reply("個々のタイプは", self.type)
                # ルームの場合
            elif self.text == "Roomid":
                if self.type == "room":
                    self.reply("ルームID", str(self.event.source.room_id))
            elif self.text == "の":
                a = ["あ", "い", "う", "え", ]
                self.reply(a[random.randrange(0, len(a), 1)])
            elif self.text == "あ":
                self.reply(
                    str(RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]))
            elif self.text == "い":
                self.reply(str(self.RUNNING_ID))
            elif self.text == "え":
                self.reply(str(RUNNING_ID_DICT))
            elif self.text == "お":
                self.reply(
                    str(RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"]))
            else:
                self.reply("たいきの実験")
            # 陽太の場合
        elif self.event.source.user_id == "Udc648d55708d9becb3a53fa8e058d2e9":
            self.reply("貴方は陽太", "通称ジブリールです。")
        elif self.event.source.user_id == "U8b0e55a1ef2c491311ce7f979f082510":
            self.reply("貴方は大倉 聖也", "たいきの現在のクラスメイトです。")
        else:
            self.reply("たいきに登録された人間以外は扱うことができません。",
                       "貴方のユーザーIDの取得が完了しました。", str(self.event.source.user_id))

        # モード終了メソッド
    def mode_fin(self):
        self.reply(self.MODE + "を終了します。")
        RUNNING_ID_DICT.pop(self.RUNNING_ID)

        # オウムモード
    def parrot_mode(self):
        self.reply(self.text)

        """ 引数の数だけ返答する（公式LINEの制限によって５つまで） """
        # リプライメソッド("送りたい文字")
    def reply(self, *args):
        line_bot_api.reply_message(self.event.reply_token, [
                                   TextSendMessage(text=v) for v in args])