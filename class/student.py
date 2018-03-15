class Student(object):
    
	def __init__(self, name, score):
	    self.__name = name
	    self.__score = score
	def get_name(self):
	    return self.__name
	def set_name(self, name):
	    self.__name = name
	def get_score(self):
	    return self.__score
	def set_score(self,score):
	    self.__score = score
bart = Student('Bart', 60)
if bart.get_score() != 60:
	print('测试失败!')
else:
	bart.set_score(90)
	if bart.get_score() != 90:
		print('测试失败!')
	else:
		print('测试成功!') 
	