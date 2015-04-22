class Animal(object):
	def output(self):
		print "Animal is a object."

class Dog(Animal):
	def output(self):
		print "Dog is an animal."

a = Animal()
a.output()
d = Dog()
d.output()
