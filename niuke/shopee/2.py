
#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param param string字符串 
# @return string字符串
#
class Solution:
    def compressString(self, param) :
        # write code here
        #定义双指针，如果下一个数字和上一一个一样 i++ 当不一样的时候，给出count=right-left+1
        out = ''
        left=0
        right=1
        param += ' '
        while left < len(param)-1 and right < len(param):
            if param[right] == param[left]:
                right += 1
            else:
                count=right-left
                out += param[left]
                if count >= 2:
                	out += str(count)
                left =right
                right =left +1
        # out += param[left]
        return out 

if __name__ == '__main__':
	s= Solution()
	print(s.compressString("shope2w"))



