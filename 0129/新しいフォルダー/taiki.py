""" イベントハンドラー(メッセージを受け取ったとき)が実行される前に初期化しておかないと動作不可能な変数 """
# モード選択用
RUNNINGID_AND_MODE = {}
# 電卓モードの数値から演算子へ入力させるための推移フラグ
num_set = False
# 計算モード演算子から数値へ入力させるための推移フラグ
num1_set = False
op_set = False
# 電卓モードの入力ミスカウンター
i = 1

class Reply:
    import method
    # モードの初期化
    MODE_ARRAY = ["コマンド", "管理者モード", "command", "こまんど", "オウムモード", "電卓モード", "計算モード", "沈黙モード"]
    def __init__(self, event):
    # 引数として受け取ったeventをself.event変数に代入
        self.event = event
    # 受け取った場所(個チャ,グルチャ,ルームチャ)をself.type変数に代入
        self.type = event.source.type
    # 受け取った文字をtext変数へ
        self.text = event.message.text
        # global RUNNINGID
        if self.type == "user":
            self.RUNNINGID = self.event.source.user_id
        elif self.type == "room":
            self.RUNNINGID = self.event.source.room_id
        elif self.type == "group":
            self.RUNNINGID = self.event.source.group_id
    # モード選択メソッド
    def mode_select(self):
        # user,room,groupのいづれかのidによって初期値を設定
        RUNNINGID_AND_MODE.setdefault(self.RUNNINGID, "デフォルトモード")
        self.MODE = RUNNINGID_AND_MODE.get(self.RUNNINGID,"キーが存在しません")

        """ モードに関わらず条件によって実行される処理 """
        if self.text in ["Command", "command"]:
            reply("[コマンド一覧]\n現在のコマンドは、\n" + self.modelist() + "の" + str(len(self.MODE_ARRAY) - 1) + "個です。", "番号は書かずに日本語を入力してください。")
        # モード変更メソッド
        elif self.MODE == "デフォルトモード":
            self.default_mode()
            """ 各モードによってすることを変更する """
        else:
            # モード選択済みの時
            if self.type in ["room", "group"]:
                if self.text in ["@bye", "退会願います", "消えろ", "帰れ", "去れ", "死ね"]:
                    reply("現在" + self.MODE + "です。", "退会させるためには、" + self.MODE + "を終了してください。")
            if self.text == self.MODE + "終了":
                self.mode_fin()
            elif self.MODE == "オウムモード":
                reply(self.text)
            elif self.MODE == "電卓モード":
                self.calc_mode()
            elif self.MODE == "計算モード":
                self.calc_mode2()
            elif self.MODE == "沈黙モード":
                pass
            elif self.MODE == "管理者モード":
                self.admin_mode()
            # 理論上ありえないと思うが念の為。
            else:
                reply("何のモードか分からん" + self.MODE)
