# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = min(nums)
#         tmp=0
#         for i in nums:
#             print(i,end='')
#             tmp = max(i,tmp +i)
#              #负数如果导致前面的子序列为负值就没有带上的意义，tmp是子序列考虑遇到负数的最大子序列和
#              #如果影响了，把前面的记录在res中
#             res = max(res,tmp) # 连续所有子序列最大子序列和
#             print(tmp,res)
#         return res 
# 

# def sumd(listd):
#     maxdata = 0
#     sumdata = 0
#     begin = 0
#     right = 0
#     for i in range(0, len(listd)):
#         if (sumdata >= 0):
#             sumdata = sumdata + listd[i]
#         else:
#             sumdata = listd[i]
#             begin = i # tmp 为负数时，前面无意义。
#         if (maxdata < sumdata):
#             maxdata = sumdata  # res 最大值的最后一次更新
#             right = i
#     print(maxdata)
#     print(listd[begin:right+1])
# sumd([-1, 2,3,-3,4,5,-6])
# ————————————————
# 版权声明：本文为CSDN博主「科大小笨」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/TuZiFaDai/article/details/95065721


def maxSubArray(nums):
    res = min(nums)
    tmp=0
    for i in range(len(nums)):
        # print(i,end='')
        

        tmp = max(nums[i],tmp +nums[i])
        if tmp <= 0:
            begin = i+1 # 放前面也可以 不过不用加1了
            # print(tmp,begin)
        if res<tmp:
            right=i
        res = max(res,tmp) 

        # print(tmp,res)
    print (res )
    print(nums[begin:right+1])
maxSubArray([-1, 2,3,-3,4,5,-6])