from sys import stdout


for i in range(0, 10):
    print "value of 'i' is: %d" % i
 
new_list = [113, 535, 535, 23, 654, 5444, 535]

for i in new_list:
    print i, 

print 

for i in new_list:
    stdout.write(str(i)) 
 
print 
print new_list[3]

