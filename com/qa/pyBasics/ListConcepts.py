name=['praveen','Ramu','Fariya','Naval','Karthik']
print(name)

#print the  lenght of  the list
print(len(name))

#print the list values for a range
print(name[2:4])


#print the elements  of the  list based on the index
print(name[0],name[4])


#print the values of the List using   the for loop
for i in name:
    print(i)


#append the values to the existing list
name.append('India')
print(name)


#append the  vakue  of the cube of 7
name.append(7**3)
print(name)


#replace the values from a range to one range
name[2:4]=['Norway','china']
print(name)




#create the nested loops
country=['china','japan','korea','india','france']
capital=['beijing','tokyo','seoul','Delhi','paris']
x=[country,capital]
print(x)

#print the values  from the perticular list
print(x[0][2],x[1][2])


