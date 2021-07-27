class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        result = 0
        length = len(s)
        myDict = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        for index in range(length):
            if index + 1 >= length or myDict[s[index + 1]] <= myDict[s[index]]:
            # if  myDict[s[index + 1]] <= myDict[s[index]]:
                result += myDict[s[index]]
            else:
                result -= myDict[s[index]]
        return result



if __name__ == '__main__':
    s=Solution()
    print(s.romanToInt('III'))



chart = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
strs = input()
result = 0
omit = -1  # omit为需省略的字符位
 
if strs in chart:
    print(chart[strs])
else:
    for i in range(len(strs)):  # 遍历字符串的每一位:(0,len-1)
        if i == omit:  # 如果无需省略i
            pass
        elif i <= len(strs)-2:  # 如果还没有遍历到最后一位:(len-1-1)
            if chart[strs[i]] < chart[strs[i+1]]:  # 如果前一位对应值小于后一位的
                result += chart[strs[i+1]] - chart[strs[i]]  # 进行减操作
                omit = i+1  # 省略下一位字符
            else:
                result += chart[strs[i]]
        else:  #  遍历到最后一位
            result += chart[strs[i]]
    print(result)
# ————————————————
# 版权声明：本文为CSDN博主「6加派」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/weixin_39406894/article/details/80468036