class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
         print('set balance')
         if not isinstance(value, (int, float)):
             raise ValueError('Баланс должен быть числом')
         self.__balance = value

    @my_balance.deleter
    def my_balance(self):
         print('delete balance')
         del self.__balance

    # my_balance = property(my_balance)
    # my_balance = my_balance.getter(get_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)
    # balance = property(fget = get_balance,
    #                    fset = set_balance,
    #                    fdel = delete_balance)

# a = BankAccount('Ivan', 100)
# # print(a.my_balance)
# a.my_balance = 9000
# print(a.my_balance)

p = BankAccount("Misha", 200)

print(p.my_balance)

p.my_balance = 905

del p.my_balance

print()

