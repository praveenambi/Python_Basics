
# creating a normal default function
def test():
    print("Hello Praveen")

test()  # calling the  test() function here to run
print("*********************************************************")

# creating a parameterised fucntion where a is the param
def sum(a):
    print(a+20)

sum(50)    # calling the sum() function here
print("***********************************************************")

#creating a optional/default parameterised function
def getCountryName(name="India"):
    print(name)

getCountryName()
getCountryName("Spain")
getCountryName(100)
print("************************************************************")

# creating a fucntion  to pass the list
def getCountryNames(list):
    for x in list:
        print(x)

countryNames =["Spain", "Italy","UK","Sweden","Norway","germany","Belgium","France"]

getCountryName(countryNames)
print("*************************************************************")

# creating a function with return statement
def summations(n,m):
    v = m+n
    return v
c = summations(2,44) # storing the return value in the variable C
print(c)
print("/********************************************************")

#creating a function with return statement  with if else condition
def getCapitalName(coutry):
    if coutry=="India":
        return "Delhi"
    elif coutry=="france":
        return "paris"

cap = getCapitalName("India")
print(cap)
print("****************************************************")

# wite a function in form of selenium
def launchBrowser(browser):
    if browser=="Firefox":
        print("Launching the firefox browser")
    elif browser=="Chrome":
        print("launching the chrome browser")
    else:
        print("there is no browser defined")

launchBrowser("Chrome") # its case sensitive, so while calling the function pass the exact value
print("************************************************************")

# recursive function in python
# recursive function is a function which call itself
# program to find the factorial of a given number using recursion

def factorial(num):
    if(num>1):
        num=num*factorial(num-1)
    return num

print(factorial(5))
print("********************************************************")

# creating a function with concatination in python
def login(userid,password):
    print("Login with userid %s and password %s" %(userid,password))
login("praveen@daimler.com","Daimler@987")