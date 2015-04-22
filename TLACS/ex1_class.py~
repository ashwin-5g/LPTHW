import math
class Point:
	def __init__(self, x=1, y=1):
		self.x = int(x)
		self.y = int(y)
		print "Co-ordinates: %d, %d" % (self.x, self.y)

	def distance_from_origin(self):
		print "Distance from orgin: %f" % (math.sqrt((self.x * self.x) + (self.y * self.y)))
try:
	while(True):
		x = raw_input("Type in the X co-ordinate: ") 
		y = raw_input("Type in the Y co-ordinate: ") 
		p = Point(x, y)
		p.distance_from_origin()
except EOFError:
	print "\nBye"
