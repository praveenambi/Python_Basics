#creating an empty class inherited by object class
class Gaurdian(object):
    pass


#create an subclass of  Gaurdian class
class Child(Gaurdian):
    pass


#test code, here is checking, whether the  child class is inherited by the parent or not
print(issubclass(Child,Gaurdian)) # here it will return True
print(issubclass(Gaurdian,Child)) #  here it will return false


#creating the objects of parent and child classes

gard= Gaurdian()
chd=Child()

# checking gard is the instance of Gaurdian class, here it will return true as it is the object of Gaurdian
print(isinstance(gard,Gaurdian))
# checking chd is the instance of Gaurdian class, here it will return true as it is the object of Child class and child class is inherited the parent class
print(isinstance(chd,Gaurdian))
# checking gard is the instance of Child class, here it will return False as it is the object of parent  class
print(isinstance(gard,Child))