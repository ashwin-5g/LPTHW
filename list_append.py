num_list = [1, 2, 3, 4, 5, 6]
more_list = [23, 45, 767, 44, 334, 'cat', 'bat', 'sat', 'fat', 'lat']
for i in more_list:
	num_list.append(i)
	
print more_list
print more_list.pop(), more_list.pop(), more_list.pop(2)
print more_list
print more_list[1], more_list[-1]

