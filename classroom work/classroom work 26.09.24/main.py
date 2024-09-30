from abc import abstractmethod

class Pet:
    def __init__(self, name: str, age: int):
        self._name:str = Pet._validate_name(name)
        self._age:int = Pet._validate_age(age)

    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return(name)
        raise Exception('Имя должно содержать только буквы')
    
    @staticmethod
    def _validate_age(age: str) -> str:
        if age > 0:
            return(age)
        raise Exception('Возраст должен быть больше 0')
    
    @abstractmethod
    def Sound(self) -> str:
        raise NotImplementedError('Нужно реализовать метод sound класса Pet')
    
    def __str__(self) -> str:
        f'{self._name}, {self._age}'



class Dog(Pet):


    def __init__(self, name: str, age: int, sound: str):
        super().__init__(name, age)
        self.sound = sound


    def __str__(self) -> str:
        return f'Собака по кличке{self._name}, возрастом: {self._age}, издает звук: {self.sound}'


p1 = Dog('Bobik', 10, 'gav')
print(p1)



