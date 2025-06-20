# class Employee:
#
#     def __init__(self, name, salary):
#         # public instance variable
#         self.name = name
#
#         # private variable
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     def set_salary(self, value):
#         self.__salary = value
#
# # creating object of a class
# emp = Employee("Ugochi Mbaekwe", 10000)
#
# # accessing public instance variable
# print("Name: ", emp.name)
#
# # accessing private instance variable
# print("Salary: ", emp._Employee__salary)
# emp.set_salary(50000)
# print("Salary: ", emp.get_salary())


# Create a class that has 2 public instance and 3 private instance variables. After,
# create two instances from the class. Display all the attributes

class Game:
    def __init__(self, name, company, sales, ceo, loss):
        self.name = name
        self.company = company

        self.__sales = sales
        self.__ceo = ceo
        self.__loss = loss

    def get_sales(self):
        return self.__sales

    def get_ceo(self):
        return self.__ceo

    def get_loss(self):
        return self.__loss


c1 = Game("Street Fighter 6", "CapCom", 2_000_000, "John Doe", 1_000_000)
c2 = Game("Marvel Rivals", "NetEase", 10_000_000, "Mary Doe", 5_000_000)

print(f''' 
Game1: {c1.name}
Company1: {c1.company}
Sale1: {c1.get_sales()}
CEO 1: {c1.get_ceo()}
Loss 1: {c1.get_loss()}''')

print(f''' 
Game2: {c2.name}
Company2: {c2.company}
Sale2: {c2.get_sales()}
CEO 2: {c2.get_ceo()}
Loss 2: {c2.get_loss()}''')

