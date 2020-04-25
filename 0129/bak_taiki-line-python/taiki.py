from linebot.models import TextSendMessage
from main import line_bot_api
import random

""" イベントハンドラー(メッセージを受け取ったとき)が実行される前に初期化しておかないと動作不可能な変数 """
# モード選択用
RUNNING_ID_DICT = {}


class Reply:
    # モードの初期化
    MODE_ARRAY = ["コマンド", "管理者モード", "command", "こまんど", "オウムモード",
                  "電卓モード", "計算モード", "沈黙モード", "財布モード", "相談モード", "特定の言葉モード"]
    SAD_WORD_ARRAY = ["死ね", "しね", "消えろ", "きえろ", "カス",
                      "かす", "クズ", "くず", "ゴミ", "ごみ", "ポンコツ", "ぽんこつ"]

    def __init__(self, event):
        # 引数として受け取ったeventをself.event変数に代入
        self.event = event
    # 受け取った場所(個チャ,グルチャ,ルームチャ)をself.type変数に代入
        self.type = event.source.type
    # 受け取った文字をtext変数へ
        self.text = event.message.text
        if self.type == "user":
            self.RUNNING_ID = self.event.source.user_id
        elif self.type == "room":
            self.RUNNING_ID = self.event.source.room_id
        elif self.type == "group":
            self.RUNNING_ID = self.event.source.group_id
    # botが使われている場所を一意に特定し、特定したIDの名前で、辞書を作成する

    # モード選択メソッド
    def mode_select(self):
        RUNNING_ID_DICT.setdefault(self.RUNNING_ID, {"モード": "デフォルトモード"})
        """ モードに関わらず条件によって実行される処理 """
        # user,room,groupのいづれかのidによって初期値を設定
        self.MODE = RUNNING_ID_DICT[self.RUNNING_ID]["モード"]
        if self.text in ["Command", "command"]:
            self.command()
        if self.text in ["@bye", "退会願います", "帰れ", "去れ"]:
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
            elif self.MODE == "オウムモード":
                self.parrot_mode()
            elif self.MODE == "電卓モード":
                self.calc_mode()
            elif self.MODE == "計算モード":
                import calculation_mode
                calculation_mode.run(self)
                # self.calc_mode2()
            elif self.MODE == "沈黙モード":
                pass
            elif self.MODE == "管理者モード":
                self.admin_mode()
            elif self.MODE == "相談モード":
                self.consultation_mode()
            elif self.MODE == "特定の言葉モード":
                self.specific_words_mode()
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

    def command(self):
        self.reply("現在使用可能なコマンドは" + str(len(self.MODE_ARRAY) - 1) + "個です。",
                   "「コマンド一覧」\n" + self.modelist(), "日本語のみを入力してください。", "例）オウムモード")

    def hira_command(self):
        self.reply("[ひらがなこまんどいちらん]\n(これはてにゅうりょくです)\nげんざいのこまんどは、\nいち、 おうむもーど\nにぃ、 でんたくもーど\nさん、 ちんもくもーど\nです。",
                   "ばんごうはかかずににほんごをにゅうりょくしてぷりーず。")
    # コマンドメソッド(コマンド一覧作成メソッド)

    def modelist(self):
        mode_list = ""
        for index in range(1, len(self.MODE_ARRAY)):
            if index <= 9:
                head = "0" + str(index)
            else:
                head = str(index)
            mode_list += "\n" + head + ". " + self.MODE_ARRAY[index]
        return mode_list
    # ～～モード終了メソッド

    def mode_fin(self):
        self.reply(self.MODE + "を終了します。")
        RUNNING_ID_DICT[self.RUNNING_ID]["モード"] = "デフォルトモード"
        RUNNING_ID_DICT.pop(self.RUNNING_ID)

    # オウムモード
    def parrot_mode(self):
        self.reply(self.text)

    # リプライメソッド("送りたい文字")
    def reply(self, *args):
        line_bot_api.reply_message(self.event.reply_token, [
                                   TextSendMessage(text=v) for v in args])
    """ 引数の数だけ返答する（公式LINEの制限によって５つまで） """

    # 相談モード
    def consultation_mode(self):
        # a = ["そうなんだね","それはしんどかったね","よく頑張ってるね","苦しいよね","辛いよね","偉い偉い","そういうときもあるよね","うんうん。"]
        import consultation_mode
        a = consultation_mode.a
        self.reply(a[random.randrange(0, len(a), 1)])

    def specific_words_mode(self):
        if self.text == "死ね":
            self.reply("なんかあったんか？", "話聞くで")
        else:
            self.reply("現在開発中です。")

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

    # 電卓モードミス時
    def mistake(self, i, num_or_op, value1, value2):
        global RUNNING_ID_DICT
        miss_msg = str(i) + "回目の失敗!!"
        if i == 1:
            self.reply(miss_msg, "それは" + num_or_op +
                       "ではありません。", num_or_op + "を入力してください")
        elif i == 2:
            self.reply(miss_msg, "...それも" + num_or_op +
                       "じゃないよ？？", num_or_op + "を入力してね！")
        elif i <= 4:
            self.reply(miss_msg, "ん～" + num_or_op +
                       "じゃないなぁ...", num_or_op + "にしようか？？")
        elif i <= 6:
            self.reply(miss_msg, "えっと、" + num_or_op + "って分かる？？", value1 +
                       "とか" + value2 + "って小学校で習わなかった？？")
        elif i <= 8:
            self.reply(miss_msg, "さては計算する気が無い！？",
                       num_or_op + "がいいなぁ。だいぶ疲れてきたよzZ")
        elif i < 10:
            self.reply(miss_msg, "いい加減にしろw", num_or_op + "入れろって言ってるやんかww")
        else:
            self.reply(str(i) + "回も失敗！！", "処理にマジで疲れたから" +
                       self.MODE + "を終了するわ。", "(つ∀-)ｵﾔｽﾐｰ")
            RUNNING_ID_DICT[self.RUNNING_ID]["モード"] = "デフォルトモード"
            RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] = 1
        RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] += 1

    # 電卓モード
    def calc_mode(self):
        global num, op, RUNNING_ID_DICT
        if "計算モード" not in RUNNING_ID_DICT[self.RUNNING_ID]:
            RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"] = {
                "最後の答え": 0, "ミス回数": 1, "ステップ": 1}
        else:
            pass
        # 電卓モードの計算処理

        if RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] == 1:
            if self.text.isdigit() == True:
                num = self.text
                RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] = 1
                RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] = 2
                self.reply("「たす」「ひく」「かける」「わる」「あまり」\nの何れかを入力してください")
            else:
                self.mistake(RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"], "数字", str(random.randrange(1, 101, 1)),
                             str(random.randrange(100, 100001, 1)))
        elif RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] == 2:
            # 演算記号の処理
            if self.text in ["たす", "ひく", "かける", "わる", "あまり"]:
                if self.text == "たす":
                    op = "+"
                elif self.text == "ひく":
                    op = "-"
                elif self.text == "かける":
                    op = "*"
                elif self.text == "わる":
                    if num == "0":
                        self.reply("0による除算は数学上不可能です。", "別の演算子を入力してください")
                        RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] = 1
                    else:
                        op = "/"
                elif self.text == "あまり":
                    if num == "0":
                        self.reply("0による除算は数学上不可能です。", "別の演算子を入力してください")
                        RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] = 1
                    else:
                        op = "%"
                # 理論上ありえない
                else:
                    self.reply(num + self.text)

                def calc(v1, op, ans_before1):
                    last_ans = eval(str(ans_before1) + op + v1)
                    answer = (str(v1) + " " + str(op) + " " +
                              str(ans_before1) + " = " + str(last_ans))
                    RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["最後の答え"] = last_ans
                    return str(answer), str(last_ans)

                answer, ans = calc(
                    num, op, RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["最後の答え"])
                self.reply("演算します", answer, "次に" + ans + "続けて演算したい数値を入力してください")
                RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] = 1
            else:
                self.mistake(
                    RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"], "指定した演算子", "たす", "ひく")
