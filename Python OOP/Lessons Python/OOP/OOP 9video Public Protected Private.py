class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name       #private методы пишутся с двумя нижними подчеркиваниями
        self.__balance = balance
        self.__passport = passport
    #
    def print_public_data(self):
        print("Sergo top")
        self.__print_private_data()

        # print(self.name, self.balance, self.passport)

    # def print_protected_data(self):  #protected методы создаются нижним подчеркиванием(программисты показывают ,что эти методы нужны
    #     print(self._name, self._balance, self._passport) #только внутри класса, но вы все равно можете к ним обратиться через другие экземпляры класса

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

    def __str__(self):
        return  f"Account {self.__name,self.__balance,self.__passport}"

class Sergo(BankAccount):
    pass

account1 = BankAccount('Bob', 100000, 4546464646)
# print(account1.print_protected_data())
print(account1.print_public_data())
print(dir(account1))
print(BankAccount('Boyyyb', 1000, 4546446))
Sergo.print_public_data
# print(account1._BankAccount__print_private_data())
# print(account1.__name)
# print(account1.__balance)
# print(account1.__passport)