from reply import RUNNING_ID_DICT
import random

# 電卓モード
def run(self):
    import mistake
    global RUNNING_ID_DICT
    if "電卓モード" not in RUNNING_ID_DICT[self.RUNNING_ID]:
        RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"] = {
            "最後の答え": 0, "ミス回数": 1, "ステップ": 1}
    else:
        pass
    # 電卓モードの計算処理
    if RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] == 1:
        if self.text.isdigit() == True:
            num = float(self.text)
            RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"] = 1
            RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] = 2
            self.reply("「たす」「ひく」「かける」「わる」「あまり」\nの何れかを入力してください")
        else:
            mistake.run(self,RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"], "数字", str(random.randrange(1, 101, 1)),
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
                last_ans = eval(str(ans_before1) + op + str(v1))
                answer = str(v1) + " " + str(op) + " " + str(ans_before1) + " = " + str(last_ans)
                RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["最後の答え"] = float(last_ans)
                return str(answer), str(last_ans)

            answer, ans = calc(num, op, float(RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["最後の答え"]))
            self.reply("演算します", answer, "次に" + ans + "続けて演算したい数値を入力してください")
            RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ステップ"] = 1
        else:
            mistake.run(self,RUNNING_ID_DICT[self.RUNNING_ID]["電卓モード"]["ミス回数"], "指定した演算子", "たす", "ひく")