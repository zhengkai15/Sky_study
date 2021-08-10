RPN_str = '1 2 + 3 4 - *'
 
stack = []
 
for c in RPN_str.split():
 
    if c in '+-*':
        i2 = stack.pop()
        i1 = stack.pop()
        print (i1,c,i2)
        print (eval('%s'*3 % (i1,c,i2)))
        stack.append(eval('%s'*3 % (i1,c,i2))) # 碰到符号就运算
    else:
        stack.append(c)
 
print ('result', stack[0])
# ————————————————
# 版权声明：本文为CSDN博主「混沌鳄鱼」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/xpresslink/article/details/77248975