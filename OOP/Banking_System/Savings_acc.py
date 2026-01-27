from Account import Account
from datetime import datetime,date

class Savings_Account(Account):
    annual_interest=0.025
    minimum_deposit=100
    
    @classmethod
    def change_interest(cls,new_interest):
        Savings_Account.annual_interest=new_interest
    
    @classmethod
    def change_min_deposit(cls,new_min_dep):
        Savings_Account.minimum_deposit=new_min_dep   
        
    
    def __inti__(self,user_name:str , phone_no:str , ssn:str ,initial_balance:float, acc_type:str):
    
        super().__init__(user_name , phone_no, ssn ,initial_balance, acc_type)
        self.__balance=0
        
        self.deposit(initial_balance)            
        
        
    def calc_interest(self):
        monthley_interest=self.__balance(self.__month_count/12)*Savings_Account.annual_interest
        self.__balance+=monthley_interest

    
    
    def deposit(self, money):
        if money <= Savings_Account.minimum_deposit:
            raise ValueError(f"Least amount of money is {Savings_Account.minimum_deposit}")
        
        super().deposit(money)
        
new=Savings_Account("mohamed",65465464,"54554",500,"savings")

#print(new.creation_date)          