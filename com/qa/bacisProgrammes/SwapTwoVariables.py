class SwapVariable:
    def doSwap(self,a,b):
        print("a is ", a," before swapping")
        print("b is " ,b,"before swapping")
        a=a+b
        b=a-b
        a=a-b
        print("a is ", a, " after  swapping")
        print("b is ",b, "after  swapping")


swap=SwapVariable()
swap.doSwap(20,30)

