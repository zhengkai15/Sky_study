# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 11:21 上午
# @Author  : Kai Zheng
# @FileName: binnarytree.py
# @Software: PyCharm
# @Email: 156252108@qq.com


# 1、判断是否是相同的树
'''
def issametree(self,p,q):
    if p == None and q == None:
        return  True
    if p == None or q == None :
        return False
    if p.val != q.val :
        return False
    return  self.issametree(p.left,q.left) and self.issametree(p.right,q.right)
'''
# 2、判断是否是对称的树
'''
def issymmetric(root):
    if root == None:
        return True
    def is_s(A,B):
        if not A and not B:
            return True
        if not A or not B or A.val != B.val:
            return False
        return is_s(A.left,B.right) and is_s(A.right,B.left)
    return is_s(root.left,root.right)
'''
# 3、二叉树的最大深度
'''
def maxDepth(root):
    if not root :
        return 0
    else:
        left_Depth= self.maxDepth(root.left)
        right_Depth= self.maxDepth(root.right)
        return max(left_Depth,right_Depth) + 1
'''



