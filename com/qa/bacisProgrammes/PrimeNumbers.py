class PrimeNum:
    def findPrime(self,num):
        flag=False

        for i in range(2, num):
            if num%i==0:
                flag=True
                print(num,"is not a Prime number")

        if not(flag):
            print(num,"is a prime number")








object=PrimeNum()
object.findPrime(13)

