class Student1(object):
    def __init__(self, name, score):
        a=name
        print("name",a)

b=Student1("zhengkai",1)
#如果不绑定self,在实例化的变量中就就访问不到这个变量
