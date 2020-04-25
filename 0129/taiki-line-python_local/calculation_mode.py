import random
from reply import RUNNING_ID_DICT
import logging
logging.basicConfig(level=logging.DEBUG)
# 計算モード


def run(self):
    global num1, num2, op, RUNNING_ID_DICT
    if "計算モード" not in RUNNING_ID_DICT[self.RUNNING_ID]:
        RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"] = {
            "最後の答え": 0, "ミス回数": 1, "ステップ": 1}
    else:
        pass
    # last_ans = RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["最後の答え"]
    # step_num = RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"]
    if RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] == 1:
        logging.debug("log3")
        if self.text.isdigit() == True:
            num1 = self.text
            RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] = 2
            RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] = 1
            self.reply("「たす」「ひく」「かける」「わる」「あまり」\nの何れかを入力してください")
        else:
            # RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] += 1
            import mistake
            mistake.run(self, RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"], "数字", str(random.randrange(1, 101, 1)),
                        str(random.randrange(100, 100001, 1)))
    elif RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] == 2:
        # 演算記号の処理
        if self.text in ["たす", "ひく", "かける", "わる", "あまり"]:
            if num1 == "0":
                if self.text == "わる" or self.text == "あまり":
                    self.reply("0による除算は数学上不可能です。", "別の演算子を入力してください")
                    RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] = 1
            elif self.text == "たす":
                op = "+"
            elif self.text == "ひく":
                op = "-"
            elif self.text == "かける":
                op = "*"
            elif self.text == "わる":
                op = "/"
            elif self.text == "あまり":
                op = "%"
            # 理論上ありえない
            else:
                self.reply(num1 + self.text)

            self.reply("２つ目の数値をで入力してください")
            RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] = 3
        else:
            # RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] += 1
            import mistake
            mistake.run(self, RUNNING_ID_DICT[self.RUNNING_ID]
                        ["計算モード"]["ミス回数"], "指定した演算子", "たす", "ひく")
    elif RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] == 3:
        if self.text.isdigit() == True:
            num2 = self.text
            RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] = 1
            # 計算モードの処理

            def calc2(v1, op, v2):
                ans_after = eval(v1 + op + v2)
                answer = (str(v1) + " " + str(op) + " " +
                          str(v2) + " = " + str(ans_after))
                return answer
            RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ステップ"] = 1
            self.reply("演算します", calc2(num1, op, num2),
                       "終了したい場合は、「計算モード終了」と言ってください。", "続けて実行する場合は１つ目の数値を入力してください")
        else:
            # RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"] += 1
            import mistake
            mistake.run(self, RUNNING_ID_DICT[self.RUNNING_ID]["計算モード"]["ミス回数"], "数字", str(random.randrange(1, 101, 1)),
                        str(random.randrange(100, 100001, 1)))
