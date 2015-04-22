class Parent(object):

	def implicit(self):
		print "Dad implicit()"

	def output(self):
		print "I am outputting stuff"


class Child(Parent):
	pass

dad = Parent()
son = Child()

son.implicit()
son.output()
