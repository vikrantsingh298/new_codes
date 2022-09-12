from typing import NamedTuple


class vikrant:
    def __init__(self, name, gender):
     self.name=name 
     self.gender= gender

    def fly(self):
        print(f"my name is {self.name}")
        print(f"my gender is {self.gender}")

class shruti():
    def __init__(self,name,gender, age):
    #def __init__(self, age):
        self.age=age

        vikrant.__init__(self,name,gender)

    def fly(self):
        vikrant.fly(self)
        print(f"my age is {self.age}")    


rounak=vikrant("rounak","male") 
abhay=shruti("abhay","male",22) 
#abhay=shruti(22)    

rounak.fly()
abhay.fly()
