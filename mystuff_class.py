class MyStuff(object):
	
	def __init__(self, line1, line2, num):
		print self
		self.tangerine = "And now a thousand years between."
		self.lines1 = line1
		self.lines2 = line2
		self.number = num
		print self
		
		
	def apple(self):
		print "I AM CLASSY APPLES!"

thing = MyStuff("This is really cool.", "This is even more cool", 33536)
print thing.tangerine
print thing.lines1
print thing.lines2
print thing.number
print
l1 = "you got another thing comin'."
l2 = "yes you do"
another_thing = MyStuff(l1, l2, 252525)
print another_thing.lines1
print another_thing.lines2
print another_thing.number
print

thing.apple()
print
print thing
print another_thing

