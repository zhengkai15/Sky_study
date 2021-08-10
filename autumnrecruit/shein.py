# -*- coding: utf-8 -*-
# @Time    : 2021/7/25 4:24 下午
# @Author  : Kai Zheng
# @FileName: dp.py
# @Software: PyCharm
# @Email: 156252108@qq.com

# shein
'''
def isVaild(str):
    # write code here
    left = '('
    right = ')'
    al = '()'
    # print(al)
    stack = []
    n = len(str)

    for i in range(n):
        if str[i] not in al:
            return False
        else:
            if str[i] == left:
                stack.append(right)
            elif stack:
                stack.pop(-1)
    return len(stack) == 0
print(isVaild('()'))
'''
# 最长递增子序列 不连续 的长度

'''
class Solution:
    def lengthOfLIS(self, nums):
        dp = []         # 用于存储每一个元素处的最大序列的长度

        n = len(nums)
        max_ = 0
        for i in range(n):
            tmp = 1
            for j in range(0,i):
                if nums[j]<nums[i]:
                    tmp = max(tmp,1+dp[j])
            dp.append(tmp)
            if max_ < tmp:
                max_ = tmp
        return max_
s= Solution()
print(s.lengthOfLIS([2,1,4,5,3]))
'''

'''
def lis(arr):
    if not arr: return 0
    n = len(arr)
    # 存放每一步规划的最大解
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:  # 如果与前面的数递增
                dp[i] = max(dp[i], dp[j] + 1)  #

    # return max(dp)
    return dp
# print(lis([2,1,4,5,3]))
# ————————————————
# 版权声明：本文为CSDN博主「少年白char」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/u011342224/article/details/107036010
'''



arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
n = len(arr)
 # 存放每一步规划的最大解
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if arr[i] > arr[j]:  # 如果与前面的数递增
            # dp[i] = max(dp[i], dp[j] + 1)  #
            dp[i] =  dp[j] + 1
print(max(dp))



'''
def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(1, n):
        for y in range( x):
            if arr[x] > arr[y] :
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    # return m
    return result
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))
'''


'''
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
n = len(arr)
m = [0] * n
for x in range(1, n):
    for y in range(0,x):
        if arr[x] > arr[y]:
            # m[x] += 1
            m[x] = m[y]+ 1
    max_value = max(m)
    result = []
    # print(m)
    print(max_value)
    for i in range(n-1,-1,-1):
        if m[i] == max_value:
            result.append(arr[i])
            max_value -= 1
# print(m)
print(result[::-1])
'''

'''
def lis(arr):
    n = len(arr)
    m = [0] * n
    for x in range(n - 2, -1, -1):
        for y in range(n - 1, x, -1):
            if arr[x] < arr[y] and m[x] <= m[y]:
                m[x] += 1
        max_value = max(m)
        result = []
        for i in range(n):
            if m[i] == max_value:
                result.append(arr[i])
                max_value -= 1
    return result


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(lis(arr))
'''

'''
arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
n = len(arr)
m = [0] * n
for x in range(n - 2, -1, -1):
    for y in range(n - 1, x, -1):
        if arr[x] < arr[y] and m[x] <= m[y]:
            m[x] += 1
    max_value = max(m)
    # print(m)
    # print(max_value)

    result = []
    for i in range(n):
        if m[i] == max_value:
            result.append(arr[i])
            max_value -= 1
print(max(m))

'''

