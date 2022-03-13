## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## dog has-a __init__ self name params  dog has-a name attribute set to name
        self.name = name
        self.owner = None
    def details(self):
        return self.name
        print("Animal: "); return self.Animal
        print("Owner: "); return self.owner
## cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ## cat  has-a __init__ self name params  cat has-a name attribute set to name
        self.name = name
        self.owner = None
    def details(self):
        print("Name: "); return self.name
        print("Animal: "); return self.Animal
        print("Owner: "); return self.owner

## person is-a object
class Person(object):

    def __init__(self, name):
        ## person has-a __init__ self name params  person has-a name attribute set to name
        self.name = name

        ## Person has-a pet attrubute set to none
        self.pet = None

## employee is-a person has-a __init__ ith self name salary params
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? super with params emploee self, has-a __init__ with name params
        super(Employee, self).__init__(name)
        ## employee has-a salary attribute set to salary
        self.salary = salary


## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet satan is-a pet
mary.pet = satan
satan.owner = mary

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet rover is-a pet
frank.pet = rover
rover.owner = frank
## flipper is-a fish
flipper = Fish()

## crouse is-a salmom
crouse = Salmon()

## harry is-a halibut
harry = Halibut()

Dog.details(rover)
#Animal.details(satan)
