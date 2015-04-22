class A(object):

	def display(self):
		print "printing from A"

	def display_two(self):
		print "printing from second function"
		print "wow, this is so cool."
		print "like, seriously."

class B(object):

	def __init__(self, num):
		self.num = num
		print "value of number is: %s" % num
	
	def display(self):
		print "printing from B"
		print "printing from B, again"

	def output(self):
		print "output from B"

class C(B, A):

	def __init__(self, num):
		self.num = num
		super(C, self).__init__(5)

	def display(self):
		print "printing from C"
		super(C, self).display_two()
		print "printing from C, again."
	

a = A()
c = C(6)

a.display()
c.display()
c.output()
