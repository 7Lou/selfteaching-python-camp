
with open('/Users/shining/Documents/GitHub/selfteaching-python-camp/19100302/7Lou/d10jieba/tang300.json','r',encoding='utf-16') as f:
    text = f.read()

import sys
sys.path.append('/Users/shining/Documents/GitHub/selfteaching-python-camp/19100302/7Lou/d10jieba/')
import stats_word_d10

try:
    print(stats_word_d10.stats_text_cn(text))

except ValueError:
    print("非字符串参数")


