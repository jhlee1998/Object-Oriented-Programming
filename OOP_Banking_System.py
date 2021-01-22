# -*- coding: utf-8 -*-
"""OOP_Banking System

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jweljj-BEliwEYtN42phIHIhpxB2G2bM
"""

class account:
  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender
    self.balance = 0
    self.transfer_amount = 0

  def deposit(self, deposit):
    self.deposit = deposit
    self.balance += self.deposit

  def withdraw(self, withdraw):
    self.withdraw = withdraw
    self.balance -= self.withdraw

  def transfer(self, receiver, transfer_amount):
    #self.receiver = receiver
    self.transfer_amount = transfer_amount
    self.balance -= self.transfer_amount
    receiver.balance += self.transfer_amount

  def display_balance(self):
    print("Account balance is ", self.balance)

peter = account("peter", 23, "male")
james = account("james", 21, "male")
peter.deposit(1000)
peter.display_balance()
peter.withdraw(500)
peter.display_balance()
peter.transfer(james, 300)
james.display_balance()
peter.display_balance()
james.deposit(100)
james.display_balance()
print(james.balance)
print(peter.transfer_amount)