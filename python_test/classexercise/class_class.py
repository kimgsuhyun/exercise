class sample : 
	a = 100
	def __init__(self):
		self.a=0
	def sample_sum(self,b):
		return self.a+b
	def sample_minus(self,b):
		return self.a-b
	def sample_X(self,b):
		return self.a*b
	def sample_4(self,b):
		if b==0:
			return 0
		else:
			return self.a/b
										# return (self.a+b)
										# c=self.a+b
										# return c  
A=sample()
print A
