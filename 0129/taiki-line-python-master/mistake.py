from reply import RUNNING_ID_DICT
# 電卓モード、計算モードミス時
def run(self, i, num_or_op, value1, value2):
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
        RUNNING_ID_DICT.pop(self.RUNNING_ID)
    if "電卓モード" in RUNNING_ID_DICT[self.RUNNING_ID]:
        RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] += 1
    elif "計算モード" in RUNNING_ID_DICT[self.RUNNING_ID]:
        RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] += 1