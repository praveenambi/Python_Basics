#here in Python , multiple Inheritance concept is allowed, unlke java, we can inherit properties from different parent classes
 #creating a father parent class
class Father(object):
     def __init__(self):
         self.fatherName="Veerabhadrappa"
         print("Father")



##creating a Mother parent class
class Mother(object):
    def __init__(self):
        self.motherName="Mahadevi"
        print("MOther")


#creating a child class inhering from both classes
# here both parent class constructers are called
class Child(Father,Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child")

    def printNames(self):
        print(self.fatherName,self.motherName)


#creating the objects of child class and test
obj=Child()
obj.printNames()