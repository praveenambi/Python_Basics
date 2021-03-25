# set  : it is not order based
# it stored the differe nt data types
# it performs different mathematical operations
#it does not stores the duplicate elements

#define a Set : use {}
s1={100,"Praveen",15.66,True}
print(s1)
s2={1,2,5,4,6,1,2,4}  # It ignores the duplicate values and print only unique  elements
print(s2)

#Set() function in python

s3=set("Python")  # storing a string , in the form of a set object
print(s3)  # out put : {'o', 'h', 't', 'y', 'P', 'n'}  # it gives the characters

s4=set([10,12,45,66,87,54,89,66])  # storing the list in the form of List , here duplicate values are allowed as its alist
print(s4)  # output : {66, 10, 12, 45, 54, 87, 89}


s5=set((15,47,85,54,22,35)) #storing the tuple in the set object
print(s5)

# while creating an set object , you can store only the strings, numbers and tuple
#List and dictionary objects are not allowed

s6={(10,20), 45,87,99}
print(s6)  # {99, 45, 87, (10, 20)}

#s7={[54,87],65,21,20,14,52,47}  # TypeError: unhashable type: 'list'  : List object are not allowed


# set operations
#union operation  :|

p1={1,2,3,4,5}
p2={3,4,5,6,7,8,9}
print(p1|p2)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}, it unions the p1 and p2
print(p1.union(p2))  # union using the function
print(p2.union(p1))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection operation
p3={1,2,3,4,5}
p4={3,4,5,6,7,8,9}
print(p3&p4)   # {3, 4, 5} , gives only the common elements
print(p3.intersection(p4))  #{3, 4, 5}print, intersection usnig the funtion
print(p4.intersection(p3))  #{3, 4, 5}

#difference of two sets  operation
p5={1,2,3,4,5,6}
p6={3,4,5,6,7,8,9}
print(p5-p6)     #{1, 2}  , it gives the  difference of the first set
print(p5.difference(p6))  # {1, 2}
print(p6.difference(p5))  #{8, 9, 7}

#symateric difference  of two sets  operation
p7={1,2,3,4,5,6}
p8={3,4,5,6,7,8,9}
print(p7^p8)    #{1, 2, 7, 8, 9}, it removed the common elements and gives other elements
print(p7.symmetric_difference(p8))  #{1, 2, 7, 8, 9}


#Set - in Built functions
#1. add()

q1={"Java","Python","C sharp","Perl","Dot net"}
q1.add("Ruby")
print(q1)   #{'Perl', 'Python', 'Ruby', 'Dot net', 'Java', 'C sharp'}

#2.Update
q2={"C++","Python","C sharp","Perl","Dot net","Java script"}
q2.update(["C","Kotlin"])
print(q2)        #{'Perl', 'Python', 'Dot net', 'C sharp', 'Java script', 'C++', 'Kotlin', 'C'}

#3.clear()
q2.clear()
print(q2)    #set()

#4. Copy()
lang={"Python","C sharp","Perl","Dot net","Java script"}
lang2=lang.copy()
print(lang2)   #{'Dot net', 'Java script', 'Python', 'Perl', 'C sharp'}  , it copies the set

#5. discard()
lang3={"Python","C sharp","Perl","Dot net","Java script"}
lang3.discard("Java script")
print(lang3)  #{'Dot net', 'C sharp', 'Perl', 'Python'}
lang3.discard("praveen")
print(lang3)    # {'Dot net', 'Perl', 'Python', 'C sharp'}, it ignores the param, and not gives any error


#6. remove()
nam={"Praveen","Ramu","naveen","Sudha","faru"}
nam.remove("Sudha")
print(nam)   #{'Praveen', 'faru', 'Ramu', 'naveen'}, sudha is removed
#now try to remove the non existing element
#nam.remove("Sonia")
#print(nam)    #KeyError: 'Sonia', remove method will give the error , as its not exist






