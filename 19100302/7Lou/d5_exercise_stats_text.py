 
text = '''
The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!
'''

#如果字符是标点符号的话就将其替换为无
pc = ".?!,:...;-()[]{}''""'*"
for i in text:
    if i in pc:  
        text = text.replace(i,"")
print(text)
#以空格切割字符串为列表    
text=text.split()
#以字典统计各个单词在文本中出现的次数
d={}
for i in text:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
#采用d.items()排序，得到包含键，值的元组的列表；这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键；reverse=True为降序
print(sorted(d.items(),key=lambda x:x[1],reverse=True))

