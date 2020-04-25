import random


# 相談モード
def consultation_mode(self):
    # a = ["そうなんだね","それはしんどかったね","よく頑張ってるね","苦しいよね","辛いよね","偉い偉い","そういうときもあるよね","うんうん。"]
    import consultation_mode
    a = consultation_mode.a
    self.reply(a[random.randrange(0, len(a), 1)])


a = ["そうなんだね", "それはしんどかったね", "よく頑張ってるね", "苦しいよね",
     "辛いよね", "偉い偉い", "そういうときもあるよね", "うんうん。"]
