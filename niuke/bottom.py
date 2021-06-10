# 再一直循环

# m=input("please input a number")


# # 写循环来获取数据，10个循环，有0就算结束。读取的数据存在列表里面，遍历出结果，打印列表
# print(100*"*")
# print(type(m))
# n=int(m)
# result=0
# if n >= 3 :
# 	n=n//3 +(n-n//3)//3
# 	result=result +n
# print(result)



n=11
result=0
# for i in range(1000000):
# 	if n >= 3 :
# 		m=n//3
# 		n=n-(n//3)*3+m
# 		result=result +m
# 	else:
# 		break
# print(result)

# while n >= 3 :
# 	m=n//3 #used
# 	n=n%3+m #
# 	result=result +m
# print(result)


"""
name: wzl
date: 2020/2/29
task:
有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。
小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？”答案是5瓶，
"""

n = int(input('please enter the bottles he owns: '))
print(n//2) # smarter solution  无限衔接下去一定会到不能换，最终只会剩下一个1，可以向老板借
if n<=0:
    x = ''
    print('please enter again.')
elif n<=1:
    x = 0
elif n<=3:
    x = 1
elif n>3:
    x = 0
    while n >3:
        a = n//3 # 换得的空瓶数
        b = n%3
        n = a+b
        x += a   # 换得的汽水瓶数
    if n == 2 or n == 3:
        x = x+1
print(x)
# ————————————————
# 版权声明：本文为CSDN博主「secx=1_cosx」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/ziluuu/article/details/104725585


for i in range(11):
    n = int(input())
    if n==1:
       print("0")
    if n==2:
       print("0")
    if n==0:
       break
    if n>=3:
       print(n//2)


