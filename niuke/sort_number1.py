def deleteDuplicatedElementFromList3(listA):
#return list(set(listA))
	return sorted(set(listA), key = listA.index)

import random
for i in range(2):
	num=int(input())
	for i in range(1,num+1):
		out_List=[]
		a=random.randrange(1,1000,1)
		out_List.append(a)
		print(deleteDuplicatedElementFromList3(out_List))





while True:
    try:
        n = int(input())
        res = set()
        for i in range(n):
            res.add(int(input()))
        for i in sorted(res):
            print(i)
    except:
        break