class Solution:
    def FindNumbersWithSum(self,array,tsum):
        if not array or not tsum:
            return 0
        front = 0
        rear =len(array)-1
        while front < rare :
            added = array[front]+array[rare]
            if added == tsum:
                return [array[front],array[rare]]
            else if : added < tsum
                front += 1
            else:
                rare -= 1
        return []
