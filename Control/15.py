# Imagine you are designing a banking application. What would a
# customer look like? What attributes would she have? What methods
# would she have?

class Customer:
    
    def __init__(self,first_name,last_name,account_no,balance,min_bal):
        self.first_name=first_name
        self.last_name=last_name
        self.account_no=account_no
        self.balance=balance
        self.min_bal= min_bal
    
    def withdraw(self,amount):
        if self.balance > amount:
            if self.balance - amount >= self.min_bal:
                self.balance -= amount
                print(f"{amount} has been deducated from {self.account_no} current balance {self.balance}")

            else:
                print(f"Can't withdraw {amount} ,{self.min_bal} minimum is required")
        else:
            print("Insufficient Balance")

    def deposit(self,amount):
        self.balance += amount

        print(f"{amount} has been deposited to your account {self.account_no}")
    
    def view_balance(self):
        print(f"The account {self.account_no} has balance {self.balance}")



c= Customer("Nitesh","Raut","101",1000,1000)
c.view_balance()
c.deposit(5000)
c.view_balance()
c.withdraw(1000)
c.view_balance()
c.withdraw(4001)