class Book:
    
    total_books=0
    def __init__(self, ISBN:str , Title:str , Publication_year: int ,Author:str , Price: float , Quantity:int):
        self._ISBN=ISBN
        self._Title=Title
        self._Publication_year=Publication_year
        self._Author=Author
        self._price=Price
        self._quantity= Quantity
        self._borrowed=0
        
        
        
    def __str__(self):
        return f"Book Title: {self._Title}\nISBN: {self._ISBN}\nPublication Year: {self._Publication_year}\nAuthor: {self._Author}\nPrice: {self._price}"        
            
    def Change_price(self,new_price:int) -> int: 
        if new_price > 0 :
            self._price=new_price
            print("Price has successfully been Changed")
        else:
            raise ValueError("Price must be positive")
    def Change_Quantity(self, new_quantity):
        self._quantity=new_quantity
    
    def Borrowed_Total(self):
        return self._borrowed
    
    def Total_Books(self):
        return self._quantity-self._borrowed    
                
    def IsAvailable(self):
        return self._borrowed < self._quantity
    
    def Borrowed(self):
        if self.IsAvailable():
           self._borrowed+=1
           Book.total_books-=1
        else:
            raise ValueError("No Copies Available")
        
    def Returned(self):
        if self._borrowed ==0:
            raise ValueError("No Books To Return!")
        self._borrowed-=1          
        Book.total_books+=1 
    
    def get_isbn(self):
        return self._ISBN 
    
    def get_name(self):
        return self._Title      
