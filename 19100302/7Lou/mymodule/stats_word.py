
def stats_text_en(text):
    """统计参数中每个英文单词出现的次数，按词频降序排列数组。"""

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
    return sorted(d.items(), key=lambda x: x[1],reverse=True)
        

def stats_text_cn(text):
    """统计参数中每个汉字出现的次数，按字频降序排列数组"""

    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型

    d={}
    for x in text:
        if '\u4e00'<=x<='\u9fa5':#通过unicode中文编码范围判定中文
            d[x] = text.count(x)
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

def stats_text(text):
    """调用stats_text_en,stats_text_cn 输出合并词频结果"""

    if not isinstance(text,str):#判断参数类型
        raise ValueError("非字符串参数")#抛出异常类型

    return(stats_text_cn(text)+stats_text_en(text))
