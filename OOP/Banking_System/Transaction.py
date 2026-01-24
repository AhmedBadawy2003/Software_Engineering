from datetime import datetime

class Transaction():
    def __init__(self,amount:float,type:str, reciever:int = None):
        self._amount=amount
        self._type=type
        self.__reciever=reciever
        self.date= datetime.now()
        