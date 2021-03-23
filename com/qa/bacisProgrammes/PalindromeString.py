class Stringpalindrome:
    def checkPalindrome(self,name):
            rev = ""
            print(name.__len__() - 1)
            for i in range(name.__len__() - 1, -1, -1):
                rev = rev + name[i]
                --i

            if name==rev:
                print(name,"is a palindrome")
            else:
                print(name,"is not palindrome")

            print(rev)




pal=Stringpalindrome()
pal.checkPalindrome('ada')
