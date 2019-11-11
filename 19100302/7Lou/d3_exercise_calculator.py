#加减乘除计算器
# 思路：分三步，输入 计算 输出 
#输入 input()函数
#计算 + - * /,提供可选择项
#输出 print()函数
x = input('请输入x:')
y = input('请输入y:')
z = input('请选择+ or - or * or /:')
if z == '+':
    print(float(x)+float(y))
elif z == '-':
    print(float(x)-float(y))
elif z == '*':
    print(float(x)*float(y))
elif z == '/':
    print(float(x)/float(y))
else:
    z != '+' or '-' or '*' or '/'
    print('Error')


