# /*
#  * @Author: Kai zheng 
#  * @Date: 2021-03-11 18:13:16 
#  * @Last Modified by: Kai Zheng
#  * @Last Modified time: 2021-03-11 18:14:14
#  */



# def B():
# 	print("hello B")
# if __name__=='__main__':
# 	B()

class zk():
	def __init__(self,A=3):
		print("hello=",A)
		self.B()
		# B()	
	def B(self,):
		print("hello B")	

if __name__ == '__main__':
	zk()





# class zk: #()不影响
# 	def __init__(self,A):
# 		print("hello=",A)
# 		self.B(4)	
# 	def B(self,B):
# 		print("hello=",4)	

# if __name__ == '__main__':
# 	zk(5)
# http://c.biancheng.net/view/2266.html
