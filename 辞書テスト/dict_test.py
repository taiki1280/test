RUNNINGID_AND_MODE = {}
def aa():
    global RUNNINGID_AND_MODE
    RUNNING_ID = "ID_aa"
    
    RUNNINGID_AND_MODE.setdefault(RUNNING_ID,{"モード" : "デフォルトモード","電卓モード" : 0})
    RUNNINGID_AND_MODE.setdefault(RUNNING_ID,{"モード" : "オウムモード","電卓モード" : 34
    })

    # RUNNINGID_AND_MODE.set([RUNNING_ID],{"a" : "c"})
    RUNNINGID_AND_MODE[RUNNING_ID]["モード"] = "あ"

    print(RUNNINGID_AND_MODE)
    print(RUNNINGID_AND_MODE[RUNNING_ID])
    # import test_im
aa()
