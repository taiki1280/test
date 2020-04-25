def run(self):
    self.DICT.setdefault("ステップ", 1)
    step = self.DICT["ステップ"]
    print(self.DICT["ステップ"])
    bbb_aaa(self)
    step += 1
    print(self.DICT["ステップ"])
    print(step)


def bbb_aaa(self):
    pass
