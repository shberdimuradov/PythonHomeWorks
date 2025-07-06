import json
import os
import itertools

# Farm Model
class Animal:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def eat(self, food_weight):
        self.weight += food_weight
        return self.weight

    def sleep(self, hours):
        return f"{self.name} sleeps for {hours} hours"

class Cow(Animal):
    def __init__(self, name, weight, milk_capacity):
        super().__init__(name, weight)
        self.milk_capacity = milk_capacity

    def milk(self):
        return self.milk_capacity

class Chicken(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)

    def lay_egg(self):
        return f"{self.name} laid an egg"

class Sheep(Animal):
    def __init__(self, name, weight, wool_amount):
        super().__init__(name, weight)
        self.wool_amount = wool_amount

    def shear(self):
        w = self.wool_amount
        self.wool_amount = 0
        return w

# Bank Application
class Account:
    def __init__(self, number, name, balance=0):
        self.number = number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        return self.balance

class Bank:
    _id_iter = itertools.count(1)
    _file = 'accounts.json'

    def __init__(self):
        self.accounts = {}
        self.load()

    def create_account(self, name, initial_deposit=0):
        num = next(self._id_iter)
        acc = Account(num, name, initial_deposit)
        self.accounts[num] = acc
        self.save()
        return num

    def view_account(self, number):
        return self.accounts.get(number)

    def deposit(self, number, amount):
        acc = self.view_account(number)
        if acc:
            acc.deposit(amount)
            self.save()
        return acc

    def withdraw(self, number, amount):
        acc = self.view_account(number)
        if acc:
            acc.withdraw(amount)
            self.save()
        return acc

    def save(self):
        data = {n: vars(a) for n, a in self.accounts.items()}
        with open(self._file, 'w') as f:
            json.dump(data, f)

    def load(self):
        if os.path.exists(self._file):
            with open(self._file) as f:
                for n, a in json.load(f).items():
                    num = int(n)
                    self.accounts[num] = Account(num, a['name'], a['balance'])
            last = max(self.accounts) if self.accounts else 0
            self._id_iter = itertools.count(last+1)

if __name__ == '__main__':
    bank = Bank()
    actions = {
        '1': ('Create', lambda: bank.create_account(input(), float(input()))),
        '2': ('View', lambda: bank.view_account(int(input()))),
        '3': ('Deposit', lambda: bank.deposit(int(input()), float(input()))),
        '4': ('Withdraw', lambda: bank.withdraw(int(input()), float(input())))
    }
    menu = "1.Create\n2.View\n3.Deposit\n4.Withdraw\n5.Exit"
    while True:
        print(menu)
        c = input()
        if c == '5': break
        func = actions.get(c)
        if func:
            print(func[1]())
        else:
            print('Invalid')
