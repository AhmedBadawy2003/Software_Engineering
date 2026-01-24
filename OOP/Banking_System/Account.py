from abc import ABC, abstractmethod
import random
from datetime import datetime, date
from Transaction import Transaction

class Account(ABC):
    acc_ids=[]
    all_accounts=[]
    
    def __init__(self,user_name:str , phone_no:str , ssn:str ,initial_balance:float, acc_type:str):
        self.user_name=user_name
        self._phone_no=phone_no
        self._ssn=ssn
        self.__balance=0
        self.acc_type=acc_type
        self.__acc_no=Account.acc_no_gen()
        self.acc_status:bool =True
        self.__history=[]
        self.deposit(initial_balance)
        Account.all_accounts.append(self)
        self._transactions_no=0
  
  
    @staticmethod    
    def acc_no_gen():
        while True:
            new_id=random.randint(1000000000, 9999999999)
            
            if new_id not in Account.acc_ids:
                Account.acc_ids.append(new_id)
                return new_id
            
   
   
    def deposit(self,money:float):
        if self.acc_status:
            if money>0:
                self.__balance+=money
                
                self.history(money, "Deposit")
            if money<=0:
                raise ValueError("insufficient amount of money") 
        else:
            raise ValueError("Account is not Active") 
   
   
    def withdraw(self,money:float):
        if self.acc_status:
            if money > self.__balance:
                raise ValueError("Your balance doesnt meet this amount")
            else:
                self.__balance-=money
             
                self.history(money, "Withdraw")
                  
        else:
            raise ValueError("Account is not Active")     
        
  
  
    def history(self,money:float,transaction:str,receiver:int =None):
        receipt = Transaction(money, transaction, receiver)
        self.__history.append(receipt)    
    
  
  
    def Transfer(self, money: float, reciever_no: int):
        if reciever_no == self.acc_no:
            print("Error: Cannot transfer to your own account.")
            return

        for acc in Account.all_accounts:
            if acc.acc_no == reciever_no:
                if money > self.balance:
                    print("Error: Insufficient funds for transfer.")
                    return
                self._Account__balance -= money
                acc._Account__balance += money
            
                self.history(money, "Transfer Out", reciever_no)
                
                acc.history(money, "Transfer In", self.acc_no)
                
                print(f"Successfully transferred ${money} to Account {reciever_no}")
                return
            
        print("No Account with this number found.")
                
  
    @abstractmethod
    def calc_interest(self):
        pass
    
  
  
    @property
    def balance(self):
      return self.__balance
    
    
    @property    
    def acc_no(self):
        return self.__acc_no
  
  
    
    def __str__(self):
        return f"User:{self.user_name}\nAccount No.:{self.__acc_no}\nBalance:{self.__balance}"
  
  
    
    def deactive_acc(self):
        self.acc_status =False
        
    def max_transaction(self):
        date=datetime.today().day  

    def __get_daily_total(self):
        today = date.today()
        total = 0.0
        for entry in self.__history:  
           if entry.date.date() == today and entry._type.lower() in ["withdraw", "transfer"]:
            total += entry._amount
        return total

print(datetime.today().date())         
print(datetime.now())




class Transaction():
    def __init__(self,amount:float,type:str, reciever:int = None):
        self._amount=amount
        self._type=type
        self.__reciever=reciever
        self.date= datetime.now()
        
    def __str__(self):
        return f"Date: {self.date}\nAmount:{self._amount}\nTransaction Type:{self._type}\nReciever:{self.__reciever}"