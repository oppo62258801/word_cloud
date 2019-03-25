#!/usr/bin/env python
# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import jieba
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


url = "https://www.sohu.com/a/226127592_139908"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')    # lxml用来解析网页

# response.status_code    # 如果返回值为200则表示访问成功

links_div = soup.find("article", class_="article")
# print(links_div)     # 我们可以尝试输出下获取的文本，验证是否是我们想要的
text = str(links_div).strip()   # 对字符串进行切片操作

# print(text)
# dic = {text}

with open("/Users/lcq-mac/code/word_cloud/reptile_word_cloud/report.txt", 'w') as f:
    f.write(text)
f.close()


# r = '[]'
request_file = open("./report.txt").read()
# request_file = re.sub(None, '', request_file)      # 剔除无关信息
request_file = request_file.replace("class", "").replace("ql", "").replace("align", "").replace("justify", "")
con = jieba.cut(request_file, cut_all=True)     # 分词
words = " ".join(con)    # 分词后插入空格
# print(words)


font_path = '/Users/lcq-mac/code/SourceHanSerifCN/SourceHanSerifCN-Regular.otf'
wordCloud = WordCloud(font_path=font_path, background_color="white", width=800, height=660).generate(words)
# 我们注意到wordcloud对中文很不友好，必须要进行jieba分词，还应该再WordCloud中增加设置字体的参数
# 否则生成的词云图片是方框型的
wordCloud.to_file('./pic.png')     # 保存图片
plt.imshow(wordCloud)
plt.axis("off")
plt.show()