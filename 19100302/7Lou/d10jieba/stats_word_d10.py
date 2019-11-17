import collections
import jieba

def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，按词频降序排列数组。"""

    i=int (input("英文词频最高的前i个词，请输入i："))
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型
    
    #通过unicode非英文字母编码范围判定非英文
    for x in text:
        if '\u005a'<x<'\u0061' or x<'\u0041' or x>'\u007a':
            text=text.replace(x," ")
        d={}
        for x in text.split():
            if x not in d:
                d[x] =1
            else:
                d[x]+=1
    return collections.Counter(d).most_common(i)
        

def stats_text_cn(text):
    """统计参数中每个汉字出现的次数，按字频降序排列数组"""

    j=int (input("中文字频最高的前j个词，请输入j："))
    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型
    text=jieba.lcut(text,cut_all = False)#生成列表
    d={}
    for x in text:
        if len(x)>=2 and '\u4e00'<=x<='\u9fa5':#通过unicode中文编码范围判定中文
            d[x] = text.count(x)
    return collections.Counter(d).most_common(j)

def stats_text(text):
    """调用stats_text_en,stats_text_cn 输出合并词频结果"""

    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型

    return(stats_text_cn(text)+stats_text_en(text))

#print(stats_text_cn(text))