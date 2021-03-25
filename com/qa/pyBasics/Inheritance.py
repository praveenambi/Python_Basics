#object class is the parent of all classes in Python, just like Java.
#so here person class is inhereting  the object class, syntax is writing the parent class in the bracket of chile class
#the syntax is like below  writtem
class Person(object):
    def __init__(self,name):
        self.name=name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False


 #creating the child class for the  Person class
class Employee(Person):

    def isEmployee(self):
        return True


#create the object of Person class and test it
prsn = Person("Praveen")
print(prsn.name)
print(prsn.getName(), prsn.isEmployee())

#create the object of the child class Employee and test it
#Throgh the child class is not having any parameter, it will call the parent class constructer and should pass the constructer argument
empl= Employee("Faru")
#since Employee is an child of parent class, it will call the construvter and pass the value argument
print(empl.name)

#since its an child class, it will inherit the methods of parent class and execute, as below getName()
print(empl.getName())

# since isEmployee() is present in both the classes, it will be overridded by the child class method, as below
print(empl.isEmployee())
