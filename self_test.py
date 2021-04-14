class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
a=Student("zhengkai",1)
print(a.name)
class Student1(object):

    def __init__(self, name, score):
        pass

b=Student1("zhengkai",1)
print(b.name)
#如果不绑定self,在实例化的变量中就就访问不到这个变量
