class Student(object):
    
	def __init__(self,name,score):
	    self.__name=name
		self.__score=score
	def get_name(self):
	    return self.__name
	def set_name(self,name):
	    self.__name=name
	def get_score(self):
	    return __score
	def set_score(self,score):
	    self.__score=score
def main()
    bart = Student('Bart', 'male')
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!') 
		