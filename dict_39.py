# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York City'
cities['OR'] = 'Portland'
cities['WA'] = 'Seattle' 

city_exist = cities.get('WY') 
print city_exist

if city_exist == None:
	print "The entry for 'WY' does not exist"
	prompt = raw_input("Do you want to create one? ")
	if prompt == "yes":
		cities['WY'] = 'Casper'
		print cities
	else:
		print "no entry added"
		
else:
	print "don't both with entry creation"

states_list = states.items()
cities_list = cities.items()

print
print cities
print 
print states
print states_list[0]
print cities_list[0]
print states_list



