def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

def cheese_crackers_sum(cheese_count, crackers_count):
    print "Sum of cheese and crackers is %d" % (cheese_count + crackers_count)


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers (10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese  + 100, amount_of_crackers + 1000)

print "We could also feed in function arguments via user input: "
cheese_user = int(raw_input("Input Cheese: "))
crackers_user = int(raw_input("Input Crackers: "))

cheese_and_crackers(cheese_user, crackers_user)

cheese_crackers_sum(cheese_user, crackers_user)
