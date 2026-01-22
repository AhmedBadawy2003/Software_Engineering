class Member:
    Max_Borrow=5
   
    total_members=0
    def __init__(self,name:str, age:int , id:str,credit:float):
        self.__name=name
        self.__age=age
        self.__id=id
        self.__credit=credit
        self.__borrowed=0
        
        
    def __str__(self)->str:
        return f"Member's Name: {self.__name}\nAge: {self.__age}\nID: {self.__id}"
    
    def Update_Info(self,name:str , age:int , id:str):
        self.__name=name
        self.__age=age
        self.__id=id
    
    def Update_ID(self,ID:str)->int:
        self.__id=ID
    
    def Update_Name(self,Name:str)->int:
        self.__name=Name
    
    def Update_age(self,age:int)->int:
        self.__age=age
    
    def Update_credit(self,credit:float):
        self.__credit+=credit
    
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name
        
            
               
    
        
            
            