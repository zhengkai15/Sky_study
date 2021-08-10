# -*- coding: utf-8 -*-
# @Time    : 2021/7/24 7:03 下午
# @Author  : Kai Zheng
# @FileName: InorderTraversal.py
# @Software: PyCharm
# @Email: 156252108@qq.com
# Definition for a binary tree node.
class Solution:
    def inorderTraversal(self, root):
        if root == None:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] +right

