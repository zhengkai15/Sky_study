class Solution:
    def jumpFloor(self,n):
        res = a = b = 1
        for i in range(n-1):
            res = a + b 
            a=b
            b= res
        return res
