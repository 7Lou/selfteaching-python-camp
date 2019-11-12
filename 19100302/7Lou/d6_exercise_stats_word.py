text='''It is the time you have wasted for your rose that makes your rose so important
你在你的玫瑰花身上耗费的时间,使得你的玫瑰花变得如此重要!!!!!!!!!。。。。、//、、、////。。!!!!The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''
import re

#统计参数中每个英文单词出现的次数，按词频降序排列数组
def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，按词频降序排列数组。"""

    text = re.sub(r'[\u4e00-\u9fa5]','',text) #替换掉中文字符
    text = re.sub(r'[^\w\s]','',text) #替换掉标调符号
    d = {}
    for x in text.split():
        if x not in d:
            d[x] =1
        else:
            d[x]+=1
    return sorted(d.items(), key=lambda x: x[1],reverse=True)


#统计参数中每个汉字出现的次数，按字频降序排列数组
def stats_text_cn(text):
    """统计参数中每个汉字出现的次数，按字频降序排列数组"""
    
    text = re.sub("[A-Za-z]", '', text)
    text = re.sub(r'[^\w\s]','',text)
    d = {}
    for x in text:
        if u'\u4e00' <= x <= u'\u9fff' :
            d[x] = text.count(x)
    
    return sorted(d.items(), key=lambda x: x[1], reverse=True) #按出现数字从大到小排列

print(stats_text_en(text))
print(dict(stats_text_cn(text)))

