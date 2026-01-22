from Book import Book
from DigitalBook import DigitalBook
from Member  import Member
class Library:
    def __init__(self, Name:str , Location: str):
        self.__name=Name
        self.__location=Location
        self.__books=[]
        self.__digital_books=[] 
        self.__members=[]        
    def __str__(self):
        return f"Library Name: {self.__name}\nLocation:{self.__location}"
    
    def add_book(self, ISBN:str , Title:str , Publication_year: int ,Author:str , Price: float , Quantity:int):
        new_book=Book(ISBN , Title, Publication_year ,Author, Price , Quantity)
        self.__books.append(new_book)
        Book.total_books+=1
        
    def add_digital_book(self, ISBN:str , Title:str , Publication_year: int ,Author:str , Price: float , Quantity:int, file_format:str, url:str,file_size:float):
        
        new_digital_book=DigitalBook(ISBN, Title, Publication_year,Author, Price, Quantity, file_format, url,file_size)
        self.__digital_books.append(new_digital_book)
        DigitalBook.total_digital_books+=1
        
    def add_member(self,name:str, age:int , id:str,credit:float):
        new_member=Member(name,age,id,credit) 
        self.__members.append(new_member)
        Member.total_members+=1
    
    def search_member(self,id:str):
        for i in range(len(self.__members)):
            if id == self.__members[i].get_id():
                return Member
        return None
    
    def search_book(self,isbn):
        for i in range(len(self.__books)):
            if isbn == self.__books[i].get_isbn():        
                return Book
        return None
    
    def search_digital_book(self,isbn):
        for i in range(len(self.__digital_books)):
            if isbn == self.__digital_books[i].get_isbn():        
                return Book
        return None
            