import random
from reply import RUNNING_ID_DICT


# 財布モード
def run(self):
    import mistake
    global money
    if "財布モード" not in RUNNING_ID_DICT[self.RUNNING_ID]:
        RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"] = {
            "現在の所持金": 0, "ミス回数": 1, "ステップ": 1}
    else:
        pass
    if self.text == "リセット":
        RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"] = {
            "現在の所持金": 0, "ミス回数": 1, "ステップ": 1}
    elif RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] == 1:
        if self.text.isdigit() == True:
            money = int(self.text)
            if money == 0 and RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] <= 3:
                if RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] == 1:
                    self.reply("流石にそれは無いやろww", "どうやって生活してるんですか...？",
                               "あなたにとってこのモードの利用価値はありますか？？")
                elif RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] == 2:
                    self.reply("え、本当に...？", "まじで...？")
                elif RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] == 3:
                    self.reply("次はないからな？？", "それでいいんだな？？")
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] += 1
            else:
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"] = int(
                    self.text)
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] = 2
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"] = 1
                self.reply("現在の所持金を", "「" + str(RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"]) +
                           "円」", "にセットしました。", "値に変更がある場合は「整数」を入力後、「たす」か「ひく」か入力してください。", "なければ「財布モード終了」と入力してください")
        else:
            import mistake
            mistake.run(self, RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"], "整数", str(
                random.randrange(1, 100, 1)), str(random.randrange(100, 10000, 1)))
    elif RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] == 2:
        if self.text.isdigit() == True:
            money = int(self.text)
            if money != 0:
                self.reply("「たす」か「ひく」か入力してください。",
                           "やっぱり変更がなければ「財布モード終了」と入力してください")
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] = 3
            else:
                self.reply("変更ないやんww", "出直しなw")
        else:
            import mistake
            mistake.run(self, RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"], "整数", str(
                random.randrange(1, 100, 1)), str(random.randrange(100, 10000, 1)))
    elif RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] == 3:
        if self.text in ["たす", "ひく"]:
            if self.text == "たす":
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"] += money
            elif self.text == "ひく":
                if money < RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"]:
                    RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"] -= money
                elif money == RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"]:
                    RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"] -= money
                    self.reply("超ギリギリだったな...", "強く生きよう。", "現在あなたの所持金は「" + str(
                        RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"]) + "円」です", "まだ、入力ミス等で値に変更がある場合は再度「整数」を入力後、「たす」か「ひく」か入力してください。", "なければ「財布モード終了」と入力してください")
                else:
                    self.reply("破産やで...", "整数の値からやり直してね。")
                RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] = 2
            # 理論上ありえない
            else:
                self.reply(money + self.text)
            self.reply(
                "現在あなたの所持金は「" + str(RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["現在の所持金"]) + "円」です", "まだ、入力ミス等で値に変更がある場合は再度「整数」を入力後、「たす」か「ひく」か入力してください。", "なければ「財布モード終了」と入力してください")
            RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ステップ"] = 2
        else:
            mistake.run(
                self, RUNNING_ID_DICT[self.RUNNING_ID]["財布モード"]["ミス回数"], "指定した演算子", "たす", "ひく")
