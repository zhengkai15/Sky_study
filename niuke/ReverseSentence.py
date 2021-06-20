class Solution:
    def ReverseSentence(self,s):
        #write code here
        return ' ' + s.split(' ')[::-1] if s.strip("") else s

