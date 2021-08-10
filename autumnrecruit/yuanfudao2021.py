# -*- coding: utf-8 -*-
# @Time    : 2021/7/28 11:38 上午
# @Author  : Kai Zheng
# @FileName: yuanfudao2021.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''
l = [2,6,4,5,3]
# print(l)
l1 = sorted(l)
# print(l)
n = len(l)
res = 0
for i in range(n):
    if l[i] != l1[i]:
        res = i
        break
print(res+ 1)
print(l.index(l1[res])+ 1)
'''
'''
s= '[]3'
#print(str)
# 从右往左，如果是数字pop 掉，res* pop（）,这个数字入栈；如果是]，pop掉之后，并pop 掉 index 0 ;res + = 1
#while str:
#    if
def slu(s):
    if s == '[]':
        return 1
    if len(s) > 2:
        if  s[-1].isdigit():
            return slu(s[:-2]) * int(s[-1])
        else:
            return slu(s[1:-2]) + 1


res  = slu(s)
print(res)
'''
'''
s= '[][[][][]2]3'
#  从右到左侧，遇到数字就入栈，遇到[] 就变加上一，两个z，一个数字 一个符号,错误
num =[]
b = []
res = 1
while s!='[]':
    if s[-1].isdigit():
        num.append(int(s[-1]))
        b.append('*')
        s= s[:-1]
    else:
        s=s[1:-1]
        num.append(1)
        b.append('+')
# print(num,b)
for i in range(len(num)):
    if b[i]== '*':
        res *= num[i]
    else:
        res += num[i]
print(res)
'''
# C(m,n) 怎么计算，枚举，m 个数字arr中找 n 数字组合成的数字 有多少种
# for i in range(m):
#     tmp = arr.pop(i)
'''
arr=[1,2,3]
for i in range(len(arr)):
    tmp = arr[0:i] + arr[i+1:]
    print(tmp)
# 递归n次？
# permutation后每个数字的前n个数字然后去重？
'''
'''
#  ohh
from itertools import  permutations
arr=[1,2,3]
tmp = []
tmp.append(list(permutations(arr,3)))
print(tmp)
'''

# 基于递归实现
'''
def jiejue(str_):
    if str_ == "":
        return 0
    if str_ == "[]":
        return 1

    num_all = 0
    while len(str_) > 2:
        if str_[:2] == "[]" and str_[2] != '[' and ']': # '[]number'
            num_all += int(str_[2]) * jiejue(str_[:2])
            str_ = str_[3:]
        elif str_[:2] == "[]" and str_[2] == '[': # '[][]'
            num_all += jiejue(str_[:2])
            str_ = str_[2:]
        else:
            stack_ = ['[']
            i = 1
            while True:
                if str_[i] == '[':
                    stack_.append('[')
                elif str_[i] == ']':
                    stack_.pop()
                    if len(stack_) == 0:
                        break
                i += 1 # 统计移动的位置。
            if i + 1 < len(str_) and str_[i + 1] != '[' and ']': # i+1位置是num
                num_all += int(str_[i + 1]) *(jiejue(str_[1:i]) + 1) # 递归中间
                str_ = str_[i + 2:]
            else: # i+1位置不是数字
                num_all += jiejue(str_[1:i]) + 1
                str_ = str_[i + 1:]

    return num_all + jiejue(str_)

print(jiejue('[[]2]3'))
# https://www.nowcoder.com/discuss/694776?type=0&order=3&pos=26&page=0&channel=-1&source_id=discuss_center_0_nctrack
'''
# 第二题


# box_str = input()

# box_str='[][[]2]3'
box_str='[[]2]'
str_stack = [] #用来记录分开的箱子的数字,会用数字替换掉入栈的东西
for i in range(len(box_str)):    #遍历str
    # print(box_str[i])
    if box_str[i] == '[':        #如果是'[' 就入栈 '['
        str_stack.append(box_str[i])
    elif box_str[i] == ']':      #如果是']' 循环
        num = 1
        while str_stack[-1] != '[': #栈的最后一个不是'['就进入循环
            num += str_stack[-1]
            str_stack.pop()
        str_stack.pop()
        str_stack.append(num) #栈的最后一个'['替换为 数字，一般是1
    else:                        #如果是其他情况（数字），栈的倒数第一个乘以这个数。
        # 并且不会一开始就与到数字
        # print(str_stack)
        str_stack[-1] = str_stack[-1]*int(box_str[i])
print(str_stack)
print(sum(str_stack))



'''
# n,m,k,x = list(map(int,input().split()))
# arr = list(map(int,input().split()))
n,m,k,x = [3,5,1,2]
arr = [1,2,3,4]
mod = 10000019

pre = [[0 for i in range(2)] for j in range(x)]
pre[0][0] = 1

for i in range(m):
    cur = [[0 for i in range(2)] for j in range(x)]
    for item in arr:
        for kk in range(x):
            cur[(kk*10+item)%x][item%2] += pre[kk][1-item%2]
            cur[(kk*10+item)%x][item%2] %= mod
    pre = cur

ans = 0
ans += pre[k][0]
ans += pre[k][1]
ans %= mod
print(ans)
'''
