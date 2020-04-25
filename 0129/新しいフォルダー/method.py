from linebot.models import TextSendMessage
from main import line_bot_api
from taiki import RUNNINGID_AND_MODE,op_set

# デフォルトモード時のメソッド
def default_mode(self):
    # RUNNINGID_AND_MODEをグローバル変数に
    global RUNNINGID_AND_MODE
    # 受け取った場所によって送信メッセージを変更
    # モード選択がされた場合
    if self.text in self.MODE_ARRAY:
        # コマンドの場合
        if self.text == "こまんど":
            self.reply("[ひらがなこまんどいちらん]\n(これはてにゅうりょくです)\nげんざいのこまんどは、\nいち、 おうむもーど\nにぃ、 でんたくもーど\nさん、 ちんもくもーど\nです。","ばんごうはかかずににほんごをにゅうりょくしてぷりーず。")
        elif self.text == "コマンド":
            self.reply("[コマンド一覧]\n現在のコマンドは、\n" + self.modelist() + "の" + str(len(self.MODE_ARRAY) - 1) + "個です。", "番号は書かずに日本語を入力してください。")
        # 沈黙モードの場合
        elif self.text in ["ちょっとうるさい", "うるさい", "黙って", "静かにしろ", "黙れ", "だまれ", "shut up", "be quiet"]:
            self.reply("今から黙ります。","沈黙モードに移行します")
            RUNNINGID_AND_MODE[self.RUNNINGID] = "沈黙モード"
        elif self.text == self.MODE:
            self.reply("今既に" + self.MODE + "やで...？")
        else:
            RUNNINGID_AND_MODE[self.RUNNINGID] = self.text
            self.MODE = self.text
            text = self.MODE + "が選択されました。\n[" + self.MODE + "終了]と言われるまで" + self.MODE + "になります。"
            # モードによって文言を追加
            if self.MODE == "電卓モード":
                global ans_before1,num_set
                ans_before1 = 0
                num_set = False
                self.reply(text, "初期値として(最初に演算される数値として)0が入っています。", "この0に対して演算したい数値と演算記号を、数値、演算記号の順に入力してください。", "最初に数値を入力してください", "例）0")
            if self.MODE == "計算モード":
                global num1_set
                num1_set = False
                self.reply(text, "演算したい１つ目の数値、演算記号、２つ目の数値を、数値、演算記号、数値の順に入力してください。", "１つ目の数値を入力してください", "例）0")
            # ない場合はそのまま
            else:
                self.reply(text)
    else:
        self.reply("This is Taiki's bot","今出来ることは「コマンド」と入力すれば一覧を表示できます。")

        """ グループ又はルームチャットの時 """
    if self.type in ["group","room"]:
        # 受け取った言葉によって退会処理
        if self.text in ["@bye", "退会願います", "消えろ", "帰れ", "去れ", "死ね"]:
            self.reply("分かりました。")
            if self.type == "group":
                line_bot_api.leave_group(self.event.source.group_id)
            else:
                line_bot_api.leave_room(self.event.source.room_id)

            """ メッセージをしてきた人間によって処理 """
        # 陽太の場合
        elif self.event.source.user_id == "Udc648d55708d9becb3a53fa8e058d2e9":
            self.reply("貴方は陽太", "通称ジブリールです。")
    else:
        self.reply("This is Taiki's bot","今出来ることは「コマンド」と入力すれば一覧を表示できます。")

# ～～モード終了メソッド
def mode_fin(self):
    self.reply(self.MODE + "を終了します。")
    RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
    # RUNNINGMOID_AND_MODE
    if self.type == "user":
        RUNNINGID_AND_MODE.pop(self.event.source.user_id)
    elif self.type == "group":
        RUNNINGID_AND_MODE.pop(self.event.source.group_id)
    elif self.type == "room":
        RUNNINGID_AND_MODE.pop(self.event.source.room_id)
# (オウムモード)
# リプライメソッド("送りたい文字")
def reply(*args):
    line_bot_api.reply_message(self.event.reply_token, [TextSendMessage(text=v) for v in args])
""" 引数の数だけ返答する（公式LINEの制限によって５つまで） """

# 管理者モード
def admin_mode(self):
    # 大樹の場合
    if self.event.source.user_id == "Uffc2e609077732c505aae085ba524938":
        # 個人チャットの時
        if self.type == "user":
            if self.text == "あ":
                self.reply(str(RUNNINGID_AND_MODE), "あなたのユーザーIDは", str(self.event.source.user_id), "です")
            else:
                self.reply("たいきの実験")
        elif self.type == "group":
            self.reply("ここはグルチャやな", "ここのグループIDは", str(self.event.source.group_id), "です")
        # ルームの場合
        elif self.type == "room":
            self.reply("ここは誰かが強制的に作ったルームチャットやな", "ここのルームIDは", str(self.event.source.room_id), "です")
        else:
            self.reply(self.type)
    else:
        self.reply("管理者以外は扱うことができません。")

# コマンドメソッド(コマンド一覧作成メソッド)
def modelist(self):
    mode_list = ""
    for index in range(1, len(self.MODE_ARRAY)):
        if index <= 9:
            head = "0" + str(index)
        else:
            head = str(index)
        mode_list += head + ". " + self.MODE_ARRAY[index] + "\n"
    return mode_list

# 電卓モードメソッド
def calc_mode(self):
    global RUNNINGID_AND_MODE,num_set,i,num,op
    if num_set == False:
        if self.text.isdigit() == True:
            num = self.text
            num_set = True
            i = 1
            self.reply("演算子をひらがな(たす,ひく,かける,わる,あまり)で入力してください")
        else:
            if i == 1:
                self.reply("それは数値ではありません。","数値を入力してください")
            elif i == 2:
                self.reply("...それも数値じゃないよ？？","数値を入力してね！")
            elif i <= 5:
                self.reply("ん～数値じゃないなぁ...","数値にしようか？？")
            elif i <= 8:
                self.reply("ん～数値って分かる？？？","１とか２とか小学校で習わなかった？？")
            elif i < 20:
                self.reply("いい加減にしろw","数値入れろって言ってるやんかww")
            else:
                self.reply("疲れたので" + self.MODE + "を終了します。","(つ∀-)ｵﾔｽﾐｰ")
                RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
                i = 1
            i += 1
    else :
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
                    self.reply("0による除算は数学上不可能です。","別の演算子を入力してください")
                    i = 1
                else:
                    op = "/"
            elif self.text == "あまり":
                op = "%"
            # 理論上ありえない
            else:
                self.reply(num + self.text)
            # 電卓モードの処理
            def calc(v1, op):
                global ans_before1
                ans_after = eval(str(ans_before1) + op + v1)
                answer = (str(v1) + " " + str(op) + " " + str(ans_before1) + " = " + str(ans_after))
                ans_before1 = ans_after
                return str(answer),str(ans_after)
            answer,ans = calc(num,op)
            self.reply("演算します",answer,"次に" + ans + "続けて演算したい数値を入力してください")
            num_set = False
        else:
            if i == 1:
                self.reply("それは指定した演算子ではありません。","指定した演算子を入力してください")
            elif i == 2:
                self.reply("...それも指定した演算子じゃないよ？？","指定した演算子を入力してね！")
            elif i <= 5:
                self.reply("ん～指定した演算子じゃないなぁ...","指定した演算子にしようか？？")
            elif i <= 8:
                self.reply("ん～指定した演算子って分かる？？？","１とか２とか小学校で習わなかった？？")
            elif i < 20:
                self.reply("いい加減にしろw","指定した演算子入れろって言ってるやんかww")
            else:
                self.reply("疲れたので" + self.MODE + "を終了します。","(つ∀-)ｵﾔｽﾐｰ")
                RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
                i = 1
            i += 1
def calc_mode2(self):
    global RUNNINGID_AND_MODE, num1_set, op_set, i, num1, num2, op
    if num1_set == False:
        if self.text.isdigit() == True:
            num1 = self.text
            num1_set = True
            i = 1
            self.reply("演算子をひらがな(たす,ひく,かける,わる,あまり)で入力してください")
        else:
            if i == 1:
                self.reply("それは数値ではありません。\n数値を入力してください")
            elif i == 2:
                self.reply("...それも数値じゃないよ？？\n数値を入力してね！")
            elif i <= 5:
                self.reply("ん～数値じゃないなぁ...\n数値にしようか？？")
            elif i <= 8:
                self.reply("ん～数値って分かる？？？\n１とか２とか小学校で習わなかった？？")
            elif i < 20:
                self.reply("いい加減にしろw\n数値入れろって言ってるやんかww")
            else:
                self.reply("疲れたので" + self.MODE + "を終了します。\n(つ∀-)ｵﾔｽﾐｰ")
                RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
                i = 1
            i += 1
    elif op_set == False :
        # 演算記号の処理
        if self.text in ["たす", "ひく", "かける", "わる", "あまり"]:
            if self.text == "たす":
                op = "+"
            elif self.text == "ひく":
                op = "-"
            elif self.text == "かける":
                op = "*"
            elif self.text == "わる":
                if num1 == "0":
                    self.reply("0による除算は数学上不可能です。","別の演算子を入力してください")
                    i = 1
                else:
                    op = "/"
            elif self.text == "あまり":
                op = "%"
            # 理論上ありえない
            else:
                self.reply(num1 + self.text)

            self.reply("２つ目の数値をで入力してください")
            op_set = True
        else:
            if i == 1:
                self.reply("それは指定した演算子ではありません。\n指定した演算子を入力してください")
            elif i == 2:
                self.reply("...それも指定した演算子じゃないよ？？\n指定した演算子を入力してね！")
            elif i <= 5:
                self.reply("ん～指定した演算子じゃないなぁ...\n指定した演算子にしようか？？")
            elif i <= 8:
                self.reply("ん～指定した演算子って分かる？？？\n１とか２とか小学校で習わなかった？？")
            elif i < 20:
                self.reply("いい加減にしろw\n指定した演算子入れろって言ってるやんかww")
            else:
                self.reply("疲れたので" + self.MODE + "を終了します。","(つ∀-)ｵﾔｽﾐｰ")
                RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
                i = 1
            i += 1
    else:
        if self.text.isdigit() == True:
            num2 = self.text
            i = 1
            # 計算モードの処理
            def calc2(v1, op, v2):
                ans_after = eval(v1 + op + v2)
                answer = (str(v1) + " " + str(op) + " " + str(v2) + " = " + str(ans_after))
                return answer
            num1_set = False
            op_set = False
            self.reply("演算します",calc2(num1, op, num2),"終了したい場合は、「計算モード終了」と言ってください。","続けて実行する場合は１つ目の数値を入力してください")
        else:
            if i == 1:
                self.reply("それは数値ではありません。","数値を入力してください")
            elif i == 2:
                self.reply("...それも数値じゃないよ？？","数値を入力してね！")
            elif i <= 5:
                self.reply("ん～数値じゃないなぁ...","数値にしようか？？")
            elif i <= 8:
                self.reply("ん～数値って分かる？？？\n１とか２とか小学校で習わなかった？？")
            elif i < 20:
                self.reply("いい加減にしろw\n数値入れろって言ってるやんかww")
            else:
                self.reply("疲れたので" + self.MODE + "を終了します。\n(つ∀-)ｵﾔｽﾐｰ")
                RUNNINGID_AND_MODE[self.RUNNINGID] = "デフォルトモード"
                i = 1
            i += 1