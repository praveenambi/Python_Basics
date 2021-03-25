
# read the  values from console
x=int(input("Please enter the value of x"))
print(x)

# if else conditions syntax
if x<0:
    print("The given number s is negative")
elif x>0:
    print("The given x is positive number")
elif X==0:
    print("The given is Zero")
else:
    print("The number is not defined ")



if True:
    print("PAss")
else:   # example for dead code
    print("Fail")



# write a program to find out the highest number

a=25
b=58
c=98

if a>b and a>c:
    print("A is the highest value given")
elif b>c:
    print("b is the highest value given")
else:
    print("c is the highest value ")



# tax calculation for entered value

price = int(input("Please enter the price of item"))

if (price<100):
    price=price+20
elif (price>=100 and price<=500):
    price=price+25
else:
    price=price+50
print("Total value of the item is " + str(price))


