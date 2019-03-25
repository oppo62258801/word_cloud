# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba

# 读入背景图片
backgroud_Image = plt.imread("./parrot.png")
# 读取要生成词云的文件
text_from_file_with_apath = open("./my_test1.txt").read()
# 通过jieba分词进行分词并通过空格分隔
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)


wl_space_split = " ".join(wordlist_after_jieba)
wl_space_split = wl_space_split.replace("user name", "").replace("#", "").replace("SHOPNAME", "").replace("name", "")
font_path = '/Users/lcq-mac/code/SourceHanSerifCN/SourceHanSerifCN-Regular.otf'
my_wordcloud = WordCloud(font_path=font_path, background_color="white", width=800, height=660).generate(wl_space_split)
# my_wordcloud = WordCloud(
#     background_color='white',    # 设置背景颜色
#     mask=backgroud_Image,        # 设置背景图片
#     max_words=3000,              # 设置最大现实的字数
#     stopwords=STOPWORDS,         # 设置停用词
#     ###########################################添加下面这行代码，同时百度，下载字体库到目录中
#     font_path='/Users/lcq-mac/code/SourceHanSerifCN/SourceHanSerifCN-Regular.otf',# 设置字体格式，如不设置显示不了中文
#     max_font_size=400,            # 设置字体最大值
#     random_state=300,            # 设置有多少种随机生成状态，即有多少种配色方案
#     scale=5,
#     width=16000,
#     height=8000
#     ).generate(wl_space_split)

# 根据图片生成词云颜色
# image_colors = ImageColorGenerator(backgroud_Image)
# my_wordcloud.recolor(color_func=image_colors)
# 以下代码显示图片
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()