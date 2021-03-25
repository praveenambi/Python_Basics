#break keyword use
state="malayalam"
for i in state:
    print(i)
    if(i=='y'):
        break

print("********************************************************")

#Continue keyword use
state="Karnataka"
for i in state:
    print(i)
    if(i=='t'):
        continue

print("********************************************************")

#break keyword use for list
countries=["Australia", "Newzealand", "Japan", "Korea", "Malaysia", "Mexico", "Canada", "USA", "Thaiwan", "Singapore"]
for j  in range(len(countries)):
    print(countries[j])
    if(countries[j]=="Canada"):
        print("I have found my country")
        break



#continue keyword in use for list
countries=["Australia", "Newzeland", "Japan", "Korea", "Malaysia", "Mexico", "Canada", "USA", "Thaiwan", "Singapore"]
for j  in range(len(countries)):
    print(countries[j])
    if(countries[j]=="USA"):
        print("I have found my country")
        continue



#break with the list of languages
lang=["Hindi", "English", "German", "French", "Mexican","chinese"]
flag=False
for index in range(len(lang)):
    print(lang[index])
    if(lang[index]=="French"):
        print("French is the most famous language in world")
        flag=True
        break
if(flag):
    print("I want to learn the french language")
