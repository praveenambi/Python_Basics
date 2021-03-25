s1="Praveen Ambi"
s2="Learn Python"

print(s1+" " + s2) # Sring concatination

print("I am in  \n bangalore")  #to write in a new line

print(s2[2:7])   #to find out the substring of a string

print("Ambi" in s1)  # to check the exist of a string ina string with in condition
print("MOhit" in s2)

print("Programm" not in s2)  # to check the presence of string with not in condition

s3=""" I this is praveen
 here and checking 
 the functinality of Pycharm"""

print(s3)

print("Hi I a am learning \"Pythoin\" language")

str = "This is develop"
print(str.capitalize())
print(str.count("Praveen"))
print(str.find("is"))

print(str.lower())

str1="  hello   "

print(str1.lstrip())
print(str1.rstrip())

str2="Canada"
print(max(str2))
print(min(str2))

str3= "I am in USA"

print(str3.replace("am", "was"))

str5="Hellow i am java here"
str6=str5.split("am")

print(str6)

str7="test"
str8="test"
print(str7 is str8)