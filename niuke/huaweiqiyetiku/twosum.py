class Solution:
    def twoSum(self,numbers,target):
        out = []
        for i in range(len(numbers)):
            for j in range(i,len(numbers)):
                if numbers[i] + numbers[j] == target:
                    out.append(i+1)
                    out.append(j+1)
                    return out


if __name__ == '__main__':
    numbers = [3,2,4]
    target = 5
    s= Solution()
    out=s.twoSum(numbers,target)
#print(out)
    print(s.twoSum(numbers,target))
