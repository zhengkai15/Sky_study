# -*- coding: utf-8 -*-
# @Time    : 2021/7/27 5:30 下午
# @Author  : Kai Zheng
# @FileName: leetcode_all.py
# @Software: PyCharm
# @Email: 156252108@qq.com


#  rome to int
'''
s = 'III'
res = 0
myDict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
for i in range(len(s)):
    # print(i) 最后一个必须相加（i + 1 == len(s)）
    if  i + 1 == len(s) or myDict[s[i]] >= myDict[s[i+1]]:
        res += myDict[s[i]]
    else:
        res -= myDict[s[i]]
print(res)
'''
#  删除数组元素
'''
nums= [2,3,4,5,6]
val = 4
# print(nums)
for i in range(len(nums) - 1, -1, -1):
    if nums[i] == val:
        nums.pop(i)
print(nums)

'''


'''
# 判断路径是否相交
def isPathCrossing(path):
    dirs = {
        "N": (-1, 0),
        "S": (1, 0),
        "W": (0, -1),
        "E": (0, 1),
    }

    x, y = 0, 0
    vis = set([(x, y)])
    print(vis)
    for ch in path:
        dx, dy = dirs[ch]
        x, y = x + dx, y + dy
        if (x, y) in vis:
            return True
        vis.add((x, y))

    return False
print(isPathCrossing("NES"))
'''
# 最后落下的蚂蚁
# 蚂蚁碰面后并不影响结果
# 直接找两侧的最后一个掉下去的蚂蚁的距离（time）



# 输出星期几
'''
import datetime
# whatday=datetime.datetime(2018,1,14).strptime("%A")

# d=datetime.datetime(2018,1,14)
# whatday=d.strftime("%A")

whatday = datetime

print(whatday)

'''

'''
# 数组中最小的绝对值。
def minmumabsdifference(arr):
    arr.sort()
    arr_sub = [arr[i+1]-arr[i] for i in  range(len(arr)-1)]
    ret = min(arr_sub)
    res = []
    for i in range(len(arr)-1):
        if arr[i+1]-arr[i] == ret:
            res.append([arr[i+1],arr[i]])
    return res

print(minmumabsdifference([5,2,1,3]))
'''

# 一共N个数字,下标表示筹码，值表示筹码的位置
# 将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
# 将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
#
'''
def minCostToMoveChips(position):
    # return min(len([i for i in position if i & 1 == 1]), len([i for i in position if i & 1 == 0]))
    ou_l = len([i for i in position if i % 2 == 0])
    ji_l = len(position) - ou_l
    return min(ou_l, ji_l)
print(minCostToMoveChips([1,1,1,1,1]))
'''

# 合并两个有序链表
# 算法：依次指针遍历两个链表，谁小就把这个值赋值给新链表的next，指针移动，另一个不移动。
# 通过递归的思想，如果两个量表有一个为空，就返回另一个链表，如果都不为空，较小的值 + 剩下的merge，
# 递归判断两个链表较小的值就行了。
# 如果是n个链表怎么递归？


'''
# 删除有序数组的重复项
# 利用快慢指针，当快指针不等于慢指针的值的时候，把快指针的值给慢指针。
def removeDepulicate(nums):
    if not nums:
        return 0
    n = len(nums)
    fast = slow = 1
    while fast < n :
        if nums[fast] != nums[fast-1]:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    # return slow
    return nums[:slow]
print(removeDepulicate([0,0,1,1,1,2,2,3,3,4]))
'''


def lengthoflastword(str):
    


print(lengthoflastword("Hello World"))
