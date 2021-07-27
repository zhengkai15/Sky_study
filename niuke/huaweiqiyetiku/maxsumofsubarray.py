class Solution:
    def maxSumofSubArray(self,array):
        #process 从前往后遍历，计算前面的sum 和 加上这个数之后的sum谁大
        if len(array) == 0：
            return None
        res =max(array)
        Sum = 0
        for i in array:
            Sum = max(Sum , Sum +i)
            res = max(res, Sum)
        return res

