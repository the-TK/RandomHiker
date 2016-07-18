# -*- coding: utf-8 -*-
import Scrape,Parse,UpdWordAt
import os

target_url = 'http://news.yahoo.co.jp'
target_id = 'editorsPick'

#Scraping結果
title_scraped_list = []
#meCab分析結果（一文ごとのリスト）
title_parsed_list = []
#meCabの単語,品詞,読み仮名
word_attribute_list=[3*[]]

#タイトルリストを取得
#ex.[不信任案めぐり与野党神経戦,衛星ひとみ 人為的ミス重なる,,,,]
title_scraped_list = Scrape.scrape(target_url,target_id)


for elem in title_scraped_list:
    #センテンスを品詞分解
    #改行付きのlistで出力
    title_parsed_list.append(Parse.execute(elem))


#titleを単語,品詞,カナのlistに分解
for title_parsed_sentence in title_parsed_list:

    #一語ずつのlist作成
    title_line= title_parsed_sentence.split(os.linesep)

    for title_sep_words in title_line:
        word_attributes= title_sep_words.replace("	",",").split(",")
        if len(word_attributes)>9:
            #print word_attributes[0]+word_attributes[1]+word_attributes[9]
            word_attribute_list.extend([word_attributes[0],word_attributes[1],word_attributes[9]])

UpdWordAt.insert()

