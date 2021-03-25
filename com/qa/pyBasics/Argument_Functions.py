# creating a normal function with 2 arguments  and calling the function
def login(username, password):
    print(username,password)

login("Praveen","Daimler")
print("***************************************************************")


#login funtion can also be called by passing the key and value arguments
login(username="PraveenAmbi",password="Daimler@456")
print("***************************************************************")

#function can be created by passing the *arg parameters
#As *arg  we can pass the n number of values and call the function
def getMarks(*arg):
    for x in arg:
        print(x)

getMarks(10,20,45,17,58,11,22,14,11,77,86,24,205,35,)
print("******************************************************************")


#function can be created by passing the keyword **args parameters as below
#**args
def getStudentMarks(**args):
    for key,value in args.items():
        print("%s==%s" %(key,value))

getStudentMarks(praveen=566, Bharati=423, Ramu=214)
print("************************************************************")

#lambda functions : Anonyms functions
#a function without name

cube= lambda x: x*x*x  # assiging the function with cube variable
print(cube(4))         #pinting the cube value


total = lambda marks: marks+50
print(total(200))
print("**************************************************************")




