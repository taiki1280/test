mode_selected()
if text == MODE + "終了":
mode_fin()
"管理者モード":
admin_mode()
"オウムモード":
parrot_mode()
"沈黙モード":
pass
"電卓モード":
import calc_mode
calc_mode.run(self)
"計算モード":
import calculation_mode
calculation_mode.run(self)
"財布モード":
import wallet_mode
wallet_mode.run(self)
"相談モード":
import consultation_mode
consultation_mode.run(self)
"特定の言葉モード":
import specific_words_mode
specific_words_mode.run(self)
"サイコロモード":
import dice_mode
dice_mode.run(self)
# 理論上ありえないと思うが念の為。
else:
reply("何のモードか分からん" + MODE)

aa = {'MODE + "終了"',a()", "b": "b()", "c": "c()"}

exec(aa["b"])
