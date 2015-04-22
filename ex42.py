## Animal is-a object 
class Animal(object):
	pass

## Dog is-a Animal 
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name)
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is an object of Cat named 'Satan'
satan = Cat("Satan")

## mary is an oject of Person whose name attribute is 'Mary'
mary = Person("Mary")

## the pet attribute of mary object is set to satan
mary.pet = satan

## frank is an oject of type Employee with 'name' attribute set to "Frank" and 'Salary' to 120000
frank = Employee("Frank", 120000)

## the attribute pet is set to rover
frank.pet = rover

## flipper is an object of type Fish
flipper = Fish()

## crouse is an oject of type Salmon
crouse = Salmon()

## harry is an object of type Halibut
harry = Halibut()


