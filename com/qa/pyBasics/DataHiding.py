class Employee:

    #hidden data or private member of the class
    __salary=75000

obj=Employee()  #object created for the class
#print(obj.__salary)  # this is not the right way of accessing the hidden private member

#how to access the hidden or private  variable  of the class
# syntax to access the variable is object and single underscore and hidden variable
#private members  of the class can be accessed outside of the class by tricky syntax
print(obj._Employee__salary)





