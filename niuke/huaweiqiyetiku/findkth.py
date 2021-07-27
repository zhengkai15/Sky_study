class Solution:
    def findKth(self,num,n,K):
        def quick_sort(num):
            if len(num) <= 1:
                return num
            pivot =num[0]
            left = quick_sort([x for x in num if x<pivot])
            right = quick_sort([x for x in num if x>pivot])
            return left + [pivot] + right
        num = quick_sort(num)
        return num[n-k]





if __name__ == '__main__':
    numbers= [1,3,5,2,2]
    num=5
    k=3
    s= Solution()
    print(s.findKth(numbers,num,k))
