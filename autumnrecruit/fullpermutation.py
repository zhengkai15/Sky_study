# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 9:04 下午
# @Author  : Kai Zheng
# @FileName: fullpermutation.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''


def AllRange(listx, start, end):
    if start == end:
        for i in listx:
            print(i,end = '')
        print()
    for m in range(start,end+1):
        listx[m],listx[start] = listx[start],listx[m]
        AllRange(listx, start+1, end)
        listx[m],listx[start] = listx[start],listx[m]
list1 = [1,2,3,4]
print(AllRange(list1,0, 3))
# ————————————————
# 版权声明：本文为CSDN博主「不服输的南瓜」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_40283816/article/details/94440096

'''


from itertools import permutations
# print(list(permutations([1, 2, 3])))
n = 4
val = 7

l =[4,0,1,3]
ll = list(permutations(l))
# print(ll)
res = []
for i in ll:
    s = ''
    for j in i:
        s += str(j)
    if s[0] != '0':
        res.append(int(s))
# print(res)
res.sort()
for i in res:
    if i % val == 0:
        print(i)
        break

