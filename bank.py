class Bank:
    credits=1000,000
    account_number=2345
    account_name="Leila"
    amount=2000000
    def __init__(self,acount_number,account_name,amount):
        self.account_number=acount_number
        self.account_name=account_name
        self.amount=amount
        
        
    def deposit(self):
         
         return f"my account number is {self.account_number} my name is {self.account_name} i want to deposit {self.amount}"
        

    def withdraw(self):
        return f"my account number is {self.account_number} my name is {self.account_name} i am to withdraw {self.amount}"
        
        
            
        
    def overdrawn(self):
       return f"my account number is {self.account_number} my name is {self.account_name} i overdrawn {self.amount} than what is in the account and it refused"