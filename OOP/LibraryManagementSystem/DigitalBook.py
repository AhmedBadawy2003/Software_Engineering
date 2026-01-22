from Book import Book

class DigitalBook(Book):

    total_digital_books=0
    def __init__(self, ISBN:str , Title:str , Publication_year: int ,Author:str , Price: float , Quantity:int, file_format:str, url:str,file_size:float):
        super().__init__(ISBN , Title , Publication_year ,Author , Price, Quantity) #inherits the Books class parameters
        
        self.__file_format=file_format
        self.__url=url 
        self.__file_size=file_size
        
        
    def __str__(self)->str:
        return f"Book Title: {self._Title}\nISBN: {self._ISBN}\nPublication Year: {self._Publication_year}\nAuthor: {self._Author}\nPrice: {self._price}\nFile Format: {self.__file_format}\nDownload_Url: {self.__url}\nFile Size;{self.__file_size}"
    
    def change_url(self,new_url):
        self.__url=new_url
    
    def Get_Url(self)->str:
        return self.__url
    
    def Check_Url(self,url)->str:
        if self.__url==url:
            return f"Correct Url"
        else:
            return f"Incorrect Url"
    def Check_Format(self,format)->str:
        if self.__file_format==format:
            return f"Correct format"
        else:
            return f"Incorrect format"
        
               