# while loop
count=0

while(count<20):
    print("Hello Praveen")
    print(count)
    count=count+1

print("-------------------------------------------------------------------------------------")

# while else loop
num=0
while(num<3):
    print("Hello Java")
    num=num+1
else:
    print("Bye java")

print("-------------------------------------------------------------------------------------")

#for loop
name=["praveen" , "Mohit" , "Sanjay" , "Lalit" , "Thabira"]
for i in name:
    print(i)

print("-------------------------------------------------------------------------------------")

#print the characters
comp="Mercedes-benz India"
for i in comp:
    print(i)


print("----------------------------------------------------")



#List with for loop

tech =["Java", "Backend" , "Android" , "IOS" , "testing"]
for index in range(len(tech)):
    print(tech[index])

print("----------------------------------------------------")


#list with for loop and else condition
countries=["Australia", "Newzeland", "Japan", "Korea", "Malaysia", "Mexico", "Canada", "USA", "Thaiwan", "Singapore"]
for index in range(len(countries)):
    print(countries[index])
else:
    print("country list is over")

print("----------------------------------------------------")

#Nested for loops
for i in range(1,7):
    for j in range(i):
        print(i, end=" ")
    print()

print("----------------------------------------------------")