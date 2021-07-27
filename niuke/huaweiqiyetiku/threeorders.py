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
        def midorder(root):
            if root == None:
                return None
            midorder(root.left)
            mid.append(root.val)
            midorder(root.right)
        def lastorder(root):
            if root == None :
                return None
            lastorder(root.left)
            lastorder(root.right)
            last.append(root.val)
        

        preorder(root)
        midorder(root)
        lastorder(root)
        out = [pre,mid,last]
        return out


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    s= Solution()
    out =s.ThreeOrders(root)
    print(out)

