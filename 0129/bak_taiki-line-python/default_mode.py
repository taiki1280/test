from taiki import Reply,RUNNING_ID_DICT


# デフォルトモード
def run(self):
    # RUNNING_ID_DICTをグローバル変数に
    global RUNNING_ID_DICT
    # 受け取った場所によって送信メッセージを変更
    # モード選択がされた場合
    if self.text in self.MODE_ARRAY:
        # コマンドの場合
        if self.text == "こまんど":
            self.hira_command()
        elif self.text == "コマンド":
            self.command()
        # 沈黙モードの場合
        elif self.text in ["ちょっとうるさい", "うるさい", "黙って", "静かにしろ", "黙れ", "だまれ", "shut up", "be quiet"]:
            self.reply("今から黙ります。", "沈黙モードに移行します")
            RUNNING_ID_DICT[self.RUNNING_ID]["モード"] = "沈黙モード"
        elif self.text == self.MODE:
            self.reply("今既に" + self.MODE + "やで...？")
        else:
            RUNNING_ID_DICT[self.RUNNING_ID]["モード"] = self.text
            self.MODE = self.text
            text = self.MODE + "が選択されました。\n「" + self.MODE + \
                "終了」\nと言われるまで" + self.MODE + "になります。"
            # モードによって文言を追加
            if self.MODE == "オウムモード":
                self.reply(text, "「command」機能のみは使えますが、他のモード選択は出来ません。\n\n注意\n「コマンド」は使用できません。",
                           "私は今貴方が発言した言葉をそのまま返すオウムです。\n好きな言葉を入力してください。", "例）あ")
            elif self.MODE == "電卓モード":
                global num_set, ans_before1
                ans_before1 = 0
                num_set = False
                self.reply(text, "初期値として(最初に演算される数値として)0が入っています。",
                           "この0に対して演算したい数値と演算記号を、\n数値\n演算記号（ひらがな）\nの順に入力してください。", "最初に数値を入力してください", "例）0")
            elif self.MODE == "計算モード":
                global num1_set
                num1_set = False
                self.reply(
                    text, "演算したい１つ目の数値、\n演算記号(ひらがな)、\n２つ目の数値を、数値、演算記号、数値の順に入力してください。", "１つ目の数値を入力してください", "例）0")
            # ない場合はそのまま
            else:
                self.reply(text)
    elif self.text in self.SAD_WORD_ARRAY:
        self.reply(self.text + "とか言うな。\n言われて悲しむ人だっているんだぞ。")
    else:
        self.reply("This is Taiki's bot", "今出来ることは「コマンド」と入力すれば一覧を表示できます。")
