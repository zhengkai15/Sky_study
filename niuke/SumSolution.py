class Solution:
#1 + 2 + 3 + 4 + n
    def Sum_solution(self,n):
        ans = n 
        tmp = ans and Sum_solution(n-1)
        ans = ans + tmp
        return ans 
