class Family ():
    def __init__(self,sname):
        self.sname = sname 


class MyFamily():
    def __init__(self,name,sname,relation,age):
        self.name = name
        self.sname = sname
        self.relation = relation
        self.age = age
        
    print("I am Jay and i an 15 years old.")
    
    def PrintDetails(self):    
        print(f"{self.name} {self.sname} is my {self.relation} and is {self.age} years old.")


Yash = MyFamily("Yash","Patil","Brother",12)
Pranav = MyFamily("Pranav", "Patil", "Cousin", 18)
Pradnya = MyFamily("Pradnya", "Patil", "Cousin", 21)
Yash.PrintDetails()
Pranav.PrintDetails()
Pradnya.PrintDetails()
