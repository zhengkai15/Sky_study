
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param petals int整型一维数组 花瓣数
# @return int整型
#
class Solution:
    def petalsBreak(self, petals) :
        # write code here
        # 遍历数组，求出每个数据需要减去2多少次2和2才能为0，以2优先:直接底板处2在加上一。每个数据次数求和。
        count = 0
        for i in range(len(petals)):
            if petals[i] == 0 :
                pass
            else:
                if petals[i] % 2 == 1:
                    count += petals[i]//2 +1
                else:
                    count += petals[i]//2
        return count

if __name__ == '__main__':
	s=Solution()
	print(s.petalsBreak([2,3,10]))