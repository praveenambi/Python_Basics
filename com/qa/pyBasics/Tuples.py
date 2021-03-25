#Tuples : is a collection of elements of any python data type
#Tuple vs List:
#1. Syntax : you  have to store teh values in tuple with (), where in list its []
#Tuple is immutable but List is mutable
#tuple is immutable means we cant change the tuple elements
names=("java","Python","Dont net","C sharp")
marks = (100,200,25,47)
employeedata=("Tom",25,'mom',25.33,True)

print(employeedata)
print(employeedata[1])
#print(employeedata[6])  # tuple index out of range

#in python backward direction index is also allowed
print(employeedata[-1])
print(employeedata[-4])


#example for list is mutable in python
# here we can change the values of an List
cities=["NewYork","Washington","manhattan","Dallas","Long beach"]
cities[4]="Ottawa"
print(cities)


#example for tuples are immutable
#here we can not change the values of the Tuples
countries=("India","Spain","France","germany","Norway")
#countries[0]="Belgium"  #TypeError: 'tuple' object does not support item assignment
print(countries) #countries[0]="Belgium"  #TypeError: 'tuple' object does not support item assignment

#del keyword
#del keyword is to delete the tuple object

#continents=("Asia","Africa","Australia","Sounth America")
#,del continents # deleting the continents tuple
#print(continents)  # NameError: name 'continents' is not defined  , as its deleted

#concatination of the tuple is availbe
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)  # (1, 2, 3, 4, 5, 6) this is the output

#tuple multiply
t3=(7,8,9)
print(t3*3)  # (7, 8, 9, 7, 8, 9, 7, 8, 9)   this is the out put

#Range slicing in tuple , like substring
t4=(10,11,12,13,147,15,16)
print(t4[1:4])    # it gives the range of values from index 1 to 4,i.e  (11, 12, 13)

#in keyword to print the element in tupple
employeedata1=("Tom",25,'mom',25.33,True)
print(25 in employeedata1)  #True
print(28 in employeedata1)  #False


#not in  to print the element in tupple
employeedata2=("Tom",25,'mom',25.33,True)
print(38 not in employeedata2)   #True

#find the lenght of tuple as below
lenght=len(employeedata2)
print(lenght)                #5 , as there are 5 values

#max number
nums=(14,25,78,36,54,88,959)
print(max(nums))   #959

# max function with strings
countries1=("India","Spain","France","germany","Norway")
print(max(countries1))  # germany  , it takes the max lenght string

# min function with strings
countries1=("India","Spain","France","germany","Norway")
print(min(countries1))  # France  , it takes the max lenght string
