# -*- coding: utf-8 -*-
# @Time    : 2021/7/20 9:18 下午
# @Author  : Kai Zheng
# @FileName: dp.py.py
# @Software: PyCharm
# @Email: 156252108@qq.com
import sys
# n = int(sys.stdin.readline().strip())
# print(n)
# 6 2 3
# 1 2 3 4 5 6
# 分数分割之后在区间内
'''
n = 6
x, y = 2, 3
scores = [1,2,3,4,5,6]
scores.sort()
for i in range(n):
    if i+1 in range(x,y+1):
        # print('hi')
        print(scores[i+1])
        break
else:
    print(-1)
'''
'''
n=5
li=[-1,2,3,10,100]
li.sort()
res=0
for i in range(0,n):
    res+=abs(li[i]-i-1)
print(res)
'''
'''
# 杨辉三角
def generate(n):
    if n == 0 :
        return []
    if n == 1 :
        return [[1]]
    if n == 2 :
        return [[1],[1,1]]
    res = [[1],[1,1]]+[[] for _ in range(n-2)]
    for i in range(2,n):
        for j in range(i+1):
            if j == 0 or j == i:
                res[i].append(1)
            else:
                res[i].append(res[i-1][j-1] + res[i-1][j])
    return res
print(generate(5))
'''

'''
def maxProfit(prices):
    if not prices:
        return None
    res = 0  # 初始化最大利润
    max_p = prices[-1]  # 初始化最大股票价格
    for i in range(len(prices) - 1, -1, -1):  # 从后往前遍历
        # print(i)
        res = max(res, max_p - prices[i])  # 更新最大利润
        max_p = max(max_p, prices[i])  # 更新最高股票价格
    return res
def maxProfit2(prices):
    if not prices:
        return  None
    res = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res += prices[i]-prices[i-1]
    return res
print(maxProfit2([7,1,5,3,6,4]))
'''

'''
# 判断是否是删除过后的子序列，遍历 s, t 中找s[i],
# 找不到就报false,找到就删除 然后直接比较两个字符串也好
def issubsequence(s,t):
    i,j = 0,0
    while i < len(s):
        while j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1 and j == len(t) -1:
                    return True
                i += 1
                j += 1

            else:
                j += 1
    return False
def isSubsequence(self, s: str, t: str) -> bool:
    i,j = 0,0
    while i < len(s):
        while j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1

            else:
                j += 1
    # print(i,j)
    # return None
    return s[i-1]==t[j-1]
def issubsequence2(s,t)
        s_len = len(s)
        t_len = len(t)

        # 定义双指针，指向 s 和 t 的初始位置
        p = 0
        q = 0

        while p < s_len and q < t_len:
            # 当 s 的字符与 t 的字符匹配时
            # 同时移动 p 和 q 指针
            if s[p] == t[q]:
                p += 1
            # 如果不匹配，只移动 q 指针，与 p 指针所对应的字符继续匹配判断
            q += 1
        # 如果 p 指针到达 s 末尾返回 True
        return p == s_len

s = "abc"
t = "ahbgdc"
print(issubsequence(s,t))
'''
'''
# 最小的攀爬次数
def minCostClimbingStairs(cost):
    n = len(cost)
    dp = [0] * n
    dp[0], dp[1] = cost[0], cost[1]
    for i in range(2, n):
        dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
    return min(dp[-2], dp[-1])

print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

def minCostClimbingStaris(cost):
    for i in range(2,len(cost)):
        cost[i] = min(cost[i-2],cost[-1]) + cost[i]
    return min(cost[-2],cost[-1])
'''

