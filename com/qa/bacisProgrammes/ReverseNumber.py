class ReverseNum:
    def reverse(self, number, rev=0):

        while not(number==0):
            reminder=number%10
            rev=(rev*10)+reminder
            number=number//10

        print("The reversed number is ",rev)

object=ReverseNum()
object.reverse(12315)


