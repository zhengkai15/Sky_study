# -*- coding: utf-8 -*-
# @Time    : 2021/7/26 9:21 下午
# @Author  : Kai Zheng
# @FileName: kuaishou.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''
n =5
l = [2,4,2,3,1]
res = 0
store = []
i = 0
while True:
    if  i not in store:
        store.append(i)
        res += 1
        i = l[l[i]-1]
        # print(i)
    else:
        break
print(len(store))
'''


# 写max_pooling

'''
n =5
l=[18,14,31,1,26]
window= 2
t = len(l) - window + 1
res=[]
for i in range(t):
    res.append(max(l[i:(i+window)]))
    # print(res,i,(i+window-1))
print(res)
'''
'''
chart = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
strs = 'IX'
result = 0
omit = -1  # omit为需省略的字符位

if strs in chart:
    print(chart[strs])
else:
    for i in range(len(strs)):  # 遍历字符串的每一位:(0,len-1)
        if i == omit:  # 如果无需省略i
            pass
        elif i <= len(strs) - 2:  # 如果还没有遍历到最后一位:(len-1-1)
            if chart[strs[i]] < chart[strs[i + 1]]:  # 如果前一位对应值小于后一位的
                result += chart[strs[i + 1]] - chart[strs[i]]  # 进行减操作
                omit = i + 1  # 省略下一位字符
            else:
                result += chart[strs[i]]
        else:  # 遍历到最后一位
            result += chart[strs[i]]
    print(result)
'''





