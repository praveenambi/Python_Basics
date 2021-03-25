#create an Parent class
class Base(object):
    def __init__(self,x):
        self.x=x


#create an child class inhertitng the Base class
class Child(Base):
    def __init__(self,x,y):
        Base.x=x  # here accessing the parent class variable and assigning the value of x
        self.y=y

    def printAges(self):
        print(Base.x,self.y)


#create an object of the child class anf test  the code
chld=Child(28,30) #passing the constructer params
chld.printAges()