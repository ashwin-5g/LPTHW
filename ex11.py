print 
print "How old are you?"
age = raw_input()
print "How tall are you?"
height = raw_input()
print "How much do you weigh?"
weight = raw_input()

print "So, you're %r years old, %r cm tall and %r kg heavy." % (age, height, weight)

sum_total = int(age) + int(height) + int(weight)
print "Total of three is: %d" % sum_total
print
