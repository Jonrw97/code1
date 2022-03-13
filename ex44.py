class Parent(object):

    def implicit(self):
        print('<<self implicant', self)
        print("Parent Implicint")
        print('>>Close self', self)

    def override(self):
        print('<<self Override', self)
        print("Parent Override")
        print('>>Close self', self)

    def altered(self):
        print('<<self Altered', self)
        print('Parent Altered')
        print('>>Close self', self)

class Child(Parent):

    def override(self):
        print('<<self Override', self)
        print('Child Override')
        print('>>Close self', self)
    def altered(self):
        print('<<self Altered', self)
        print('Before child super altered')
        super(Child,self).altered()
        print('After child super altered')
        print('>>self Altered close', self)



dad = Parent()
son = Child()

dad.implicit()
son.implicit()
print('\n')

dad.override()
son.override()
print('\n')

dad.altered()
son.altered()
