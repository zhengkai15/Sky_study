# @Author: ZhengKai
# @Date:   2021-06-10 10:55:35
# @Last Modified by:   ZhengKai
# @Last Modified time: 2021-06-10 11:09:19
# get number,get random number  and then sort

def deleteDuplicatedElementFromList3(listA):
    #return list(set(listA))
    return sorted(set(listA), key = listA.index)

import random
out_List_out=[]
while True:
    num=int(input())
    for i in range(1,num+1):
    	out_List=[]
    	a=random.randrange(1,1000,1)
    	out_List.append(a)
    	# print(out_List)
    	out_List_out=out_List_out+out_List
    # tmp=sorted(out_List_out)
    # print(tmp)
    print(deleteDuplicatedElementFromList3(out_List_out))


