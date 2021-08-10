# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 7:03 下午
# @Author  : Kai Zheng
# @FileName: InorderTraversal.py
# @Software: PyCharm
# @Email: 156252108@qq.com
# Definition for a binary tree node.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        num =len(s)
        if num==1:
            return s
        ret =[]
        for i in range(0,num):
            for j in range(i+1,num+1):
                tmp=s[i:j+1]
                # print(tmp)
                # print(i,j)
                if tmp==tmp[::-1]:
                    ret.append(tmp)
        
        b=[]
        # print(ret)
        for i in ret:
            b.append(len(i))
        return ret[b.index(max(b))]



class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0]*len(s) for _ in range(len(s))]
        # print(dp)
        max_len= 0
        max_start=0
        for right in range(len(s)):
            for left in range(right+1):
                if right - left < 2 :
                    dp[left][right] = (s[left]==s[right])
                else:
                    dp[left][right] =  (s[left]==s[right]) and dp[left+1][right-1]
                if dp[left][right]  and  right - left +1 > max_len:
                    max_len = right - left +1
                    max_start = left
        return s[max_start:max_start+max_len]
