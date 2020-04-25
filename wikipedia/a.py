import wikipedia

send_message = "夢"
# 正常に検索結果が返った場合
try:
    wikipedia.set_lang("ja")  # 追加
    wikipedia_page = wikipedia.page(send_message)
    # wikipedia.page()の処理で、ページ情報が取得できれば、以下のようにタイトル、リンク、サマリーが取得できる。
    wikipedia_title = wikipedia_page.title
    wikipedia_url = wikipedia_page.url
    wikipedia_summary = wikipedia.summary(send_message)
    reply_message = '【' + wikipedia_title + '】\n' + wikipedia_summary + '\n\n' + '【詳しくはこちら】\n' + wikipedia_url
# ページが見つからなかった場合
except wikipedia.exceptions.PageError:
    reply_message = '【' + send_message + '】\nについての情報は見つかりませんでした。'
# 曖昧さ回避にひっかかった場合
except wikipedia.exceptions.DisambiguationError as e:
    disambiguation_list = e.options
    reply_message = '複数の候補が返ってきました。以下の候補から、お探しの用語に近いものを再入力してください。\n\n'
    for word in disambiguation_list:
        reply_message += '・' + word + '\n'
print(reply_message)