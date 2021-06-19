class Solution(object):
	def TreeDepth(self,pRoot):
		if not pRoot:
			return 0
		left=self.TreeDepth(pRoot.left)
		right=self.TreeDepth(pRoot.right)
		return max(left,right)+1
		