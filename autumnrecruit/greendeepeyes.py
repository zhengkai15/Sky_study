# -*- coding: utf-8 -*-
# @Time    : 2021/7/31 8:43 下午
# @Author  : Kai Zheng
# @FileName: greendeepeyes.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''
n = 6
pro = [[1, 6], [2, 3], [3, 3], [2, 3], [2, 3], [3, 7]]
res = 1
for i in range(n):
    if pro[i][0] == 1:
        res +=  pro[i][1]
    elif pro[i][0] == 2:
        res *=  pro[i][1]
    else:
        res //=  pro[i][1]
print(res)
'''
# 算法：遍历目标框数;从目标框的起始点，向下，向右侧while循环，（循环条件判断是否超过目标框）,vertical 0, herital,0->1,都是1->4,
# 总结：verti +1 mul heri +1
# 需要的变量 count 来记每个数字，res 记录最终结果,怎么去掉重复的结果？
# 做不了矩阵，数字直接和index是相关关系。
l1 = [1, 1, 1, 1, 1, 13, 10]
l2 = [9,4,1,1]
w,h,s,t,k,p,q= l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6]
# print(h)
X,Y,W,H =l2[0],l2[1],l2[2],l2[3]
#定义函数：verti heri 和res 之间的关系
def getgrid(verti,herti):
    return (verti+1)*(herti+1)

res = 0
for i in range(k):
    heri = 0
    verti = 0
    for i in range(p//s):
        if i*s > X and i*s < X + W:
            heri += 1
    for j in range(q//t):
        if q*t > X and q*t < Y + H:
            verti += 1
res += getgrid(heri,verti)
print(res)






