class StringReverse:

    def reverseString(self,name):
        rev = ""
        print(name.__len__()-1)
        for i in range(name.__len__()-1,-1,-1):
            rev=rev+name[i]
            --i

        print(rev)


object=StringReverse()
object.reverseString('praveen')
