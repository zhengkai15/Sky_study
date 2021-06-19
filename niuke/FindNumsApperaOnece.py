class Solution:
	def FindNumsApperarOnce(self,array):
        data=set()
        for d in arry:
            if d in data:
                data.remove(d)
            else:
                data.add(d)
        return list(data)
