class Solution:
    def threeOrders(self , root ):
        # write code here
        
        preorder, inorder, postorder = [], [], []
        def find(root):
            if not root:
                return None
            preorder.append(root.val)
            find(root.left)
            inorder.append(root.val)
            find(root.right)
            postorder.append(root.val)
        find(root)
#         return postorder
        return [preorder,inorder,postorder]


