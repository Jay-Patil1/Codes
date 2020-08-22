class Person:
    def __init__ (self,name,salary,role):
        self.name = name
        self.salary = salary
        self.role = role
    
    def PrintDetails(self):
        print(f"Name : {self.name}\nRole : {self.role}\nSalary : {self.salary}")


Jay = Person("Jay", 123, "Student 9th std")
Yash = Person("Yash", 123, "Student 7th std")
Ajit = Person("Ajit", 12345, "IT Solutions")
# Jay.PrintDetails()
# Yash.PrintDetails()
# Ajit.PrintDetails()
Jay.role = "Student 10th Std"
Yash.role = "Student 8th Std"
Ajit.role = "IT SOLUTIONS"
# print(Yash.role)
Jay.PrintDetails()
Yash.PrintDetails()
Ajit.PrintDetails()

                                ###EXPERIMENT###

# class Employee:
#     no_of_leaves = 8
#     var = 8
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole


#     def printdetails(self):
#         return(f"Name is {self.name}, Salayr is {self.salary} and Role is {self.role}")

#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves

#     @classmethod
#     def from_dash(cls, string):
#         return cls(*string.split("-"))

#     @staticmethod
#     def printgood(string):
#         print("This is good " + string)

# class Player:
#     no_of_games = 4
#     var = 9
#     def __init__(self, name, game):
#         self.name = name
#         self.game = game

#     def printdetails(self):
#         return (f"Name is {self.name}, Game is {self.game}")

# class CoolProgrammer(Player,Employee): # This gets access to the methods, variables, etc. for the () class.
#     language = "C++"
#     def printLanguage(self):
#         return(self.language)


# harry = Employee("Harry",355, "Instructor")
# rohan = Employee("Rohan",555, "Student")

# shubham = Player("Shubham", ["Cricket"])

# karan = CoolProgrammer("Karan",["Cricket"])  # When two classes are inherited in other it goes to the classes to get the constructor.
# det = karan.printLanguage()
# print(det)
# print(karan.var) # If a method in two editors is used then the first given class is considered.
# karan.language = ["C++", "Python", "C"]
# print(karan.language)
