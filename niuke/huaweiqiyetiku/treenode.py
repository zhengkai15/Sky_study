class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
#class ListNode:
#    def __init__(self,x):
#        self.next = None
#        self.val = x
class Solution:
    def ThreeOrders(self,root):
        pre, mid, last = [], [], []
        def preorder(root):
            if root == None:
                return None
            pre.append(root.val)
            preorder(root.left)
            preorder(root.right)


        preorder(root)
        out = pre
        return out


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    s= Solution()
    out =s.ThreeOrders(root)
    print(out)

