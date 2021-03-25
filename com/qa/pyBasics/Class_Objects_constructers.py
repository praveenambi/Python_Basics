class car:
    #class variables
    wheels=4

    #constructer of this class : defince using the __init keyword
    def __init__(self,color):  #always the self keyword is madatory in python  for any method in the class
        print("car class constructer")
        self.color=color
        print("The given color is " +color)

    # always the latest constructer will  be called and constructer overloading is not possible in python like java
    def __int__(self):
        print("this is second constructer")


    def test(self):   #self keyword is mandatery for the method inside the class
        print("test method")

    # the variables defined inside method or constructer are called  the instance variables
    def setPrice(self,price):
        self.price=price
        print("The price of the car is "+ price.__str__())

    def getPrice(self):
        return self.price


#how to create the object of this class
#just assign a variable to the class and pass the parameter of constructer as its parameterised
obj=car("Blue")
print(obj.wheels)   #accessing thr class variables byt the object reference
print(car.wheels)   # we can access the  class variablesb directly class name , there is no static and non static concept in python like java]

#how to call the methods of the class by using the object reference
obj.test() # no need to pass any parameters as its an default method
obj.setPrice(1250000)
obj.getPrice()

#we can create multiple objects like below
obj2=car()
obj2.test()



#how to a blank class in python
#just write the "pass" keyword  and it becomes an blank class
class bike:
    pass


