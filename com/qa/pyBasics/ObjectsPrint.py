#String representation  of the object
#oject printing concepts

class Mercedes():

    def __init__(self,color,model):
        self.color=color
        self.model=model

    def __repr__(self):
        return  "color:%s  model:%s" % (self.color,self.model)

    def __str__(self):
        return "value  of color is %s and value of model is %s" %(self.color,self.model)


#outside of the class and creating the  object of the class
obj=Mercedes("black",2020)
print(obj)

#if we try to print the object  then either we have to call the representation method or the str method
#when both the methods are present, by default __str method will be called

