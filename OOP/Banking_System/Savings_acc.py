from Account import Account

class Savings_Account(Account):
    def __inti__(self,user_name:str , phone_no:str , ssn:str ,initial_balance:float, acc_type:str):
    
        super().__init__(user_name , phone_no, ssn ,initial_balance, acc_type)
        