# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import sys


def download_site_imgs(url, path):
    img_urls = []

    # パス（保存先）が存在しなければ新規作成
    if not os.path.exists(path):
        os.makedirs(path)

    # htmlのパース
    soup = BeautifulSoup(requests.get(url).content, 'lxml')

    # 画像リンクなら(拡張子がjpgなど)リストに追加
    for img_url in soup.find_all("img"):
        # imgタグのsrc要素を抽出
        src = img_url.get("src")
        #src要素に画像の拡張子が含まれていたらリストに追加
        if 'jpg' in src:
            img_urls.append(src)
        elif 'png' in src:
            img_urls.append(src)
        elif 'gif' in src:
            img_urls.append(src)

    # 画像リンク先のデータをダウンロード
    for img_url in img_urls:
        re = requests.get(img_url)
        print('Download:', img_url)
        with open(path + img_url.split('/')[-1], 'wb') as f:  # imgフォルダに格納
            f.write(re.content)


if __name__ == '__main__':
    download_site_imgs(
        'https://www.google.com/search?q=%E3%82%B9%E3%83%9E%E3%83%96%E3%83%A9%E3%82%AD%E3%83%A3%E3%83%A9%E7%94%BB%E5%83%8F&rlz=1C1GCEU_jaJP853JP854&hl=ja&sxsrf=ALeKk01cxGVLyKvmjKmQD9FWW9wvGLO8qQ:1583569884953&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj7zODD-YfoAhWJ7WEKHeXdAr8Q_AUoAXoECAwQAw&biw=1280&bih=616&dpr=1.5',
        'img/')
    # download_site_imgs('https://su-gi-rx.com/archives/838', 'img/')
    # download_site_imgs('https://algorithm.joho.info/', 'img/')