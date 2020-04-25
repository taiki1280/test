RUNNING_ID = "a1"
RUNNING_ID_DICT = {}
RUNNING_ID_DICT.setdefault(RUNNING_ID,{"計算モード" : {"最後の答え" : 0,"ミス回数": 0,"ステップ" : 1}})
RUNNING_ID_DICT[RUNNING_ID]["計算モード"]["ステップ"] += 1
if RUNNING_ID_DICT[RUNNING_ID]["計算モード"]["ステップ"] == 2:
    print(RUNNING_ID_DICT)