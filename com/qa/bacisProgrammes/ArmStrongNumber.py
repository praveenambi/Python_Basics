class ArmStrong:
    def checkArmStong(self,number):
        originNum=number
        armnumber=0
        while not(number==0):
            reminder=number%10
            armnumber=armnumber+(reminder*reminder*reminder)
            number=number//10

        print(armnumber)

        if originNum==armnumber:
            print("The number is armstrong number")
        else:
            print("The original number is not armstrong")


object=ArmStrong()
object.checkArmStong(153)