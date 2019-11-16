
with open('/Users/shining/Documents/GitHub/selfteaching-python-camp/19100302/7Lou/d9标准库/tang300.json','r',encoding='utf-16') as f:
    text = f.read()

import sys
sys.path.append('/Users/shining/Documents/GitHub/selfteaching-python-camp/19100302/7Lou/d9标准库/')
import stats_word_d9

try:
    print(stats_word_d9.stats_text_cn(text))

except ValueError:
    print("非字符串参数")


