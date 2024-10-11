import sys
class customer:
    """ customer class with bank operations""" 
    bankname = 'Jidipally Manaswi'
    def _init_(self,name,balance=0.0):
        self.name = name
        self.balance = balance
        def deposit(self,amount):
            self.balance = self.balance + amount
            print('balance after deposit:', self.balance)
        def withdraw(self,amount):
            if  amount > self.balance:
                print('insufficient funds')
                sys.exit()
                self.balance = self.balance - amount
                print('balance after withdraw:',self.balance)
                print('welcome to',customer.bankname)
                name = input('enter your name:')
                c = customer(name)
                while True:
                    print('d-deposit\nw-withdraw\ne-exit')
                    option = input('choose your option:')
                    if option.lower()=='d':
                        amount=float(input('Enter your amount:'))
                        c.deposit(amount)
                    elif option.lower()=='w':
                        amount=float(input('Enter your amount:'))
                        c.withdraw(amount)
                    elif option.lower()=='e':
                        print('thanks for banking')
                        sys.exit()
                    else:
                        print('invalid option...choose valid option')
            
