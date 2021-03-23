class FactorsOfnumber:
    def findFactor(self,num):
        for i in range(1,num):
            if num%i==0:
                print(i,"is the factor of the given number")




object=FactorsOfnumber()
object.findFactor(10)