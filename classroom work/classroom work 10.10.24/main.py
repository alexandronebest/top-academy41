# class Complex:
#     def __init__(self, real: float, im: float ):
#         self.__real: float = real
#         self.__im: float = im
    
#     def __add__(self, other: Complex) -> Complex:
#         return Complex(self.__real - other.__real, self.__im - other.__im)
    
#     def __sub__(self, other: Complex) -> Complex:
#         return Complex(self.real - other.__real, self.__im - other.__im)

#     def __str__(self) -> str:
#         sign = '+' if self.__im >=0 else '-'
#         return f'{self.__real}{sign} imatch.fabs({self.__im})'


# class Library:
#     def __init__(self, name: str, author: str):
#         self.name = name
#         self.author = author

#     def __str__(self) -> str:
#         return f'{self.name},{self.author}'
    

# class Book(Library):
#     def __init__(self, name: str, author: str, publisher: str):
#         super().__init__(name, author)
#         self.publisher = publisher







class VideoLibrary:
    def __init__(self, id: int, name: str, taken: bool = False):
        self.__id: int = id
        self._name: str = name
        self.__taken:bool = taken

    @property
    def id(self):
        return self.__id
    
    def is_taken(self):
        return self.__taken
    
    def change_status(self):
        self.__taken = not self.__taken


class Movie(VideoLibrary):
    def __init__(self, id: int, name: str, taken: bool = False):
        super().__init__(id, name, taken)
    




    #     self.items: list[Item] = []

    # def add(self, Item: Item):
    #     self.__items.append(Item)

    # def find(self, id: int) -> item:
    #     for Item in self.__items:
    #         if item.id == id:
    #             return Item
            

