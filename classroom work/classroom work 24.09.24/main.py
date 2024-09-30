class Human:
    def __init__(self, name: str, age: int):
        self._name:str = Human._validate_name(name)
        self._age: int = Human._validate_age(age)


    @staticmethod
    def _validate_name(name: str) -> str:
        if name.isalpha():
            return(name)
        raise Exception('Имя должно содержать только буквы.')


    @staticmethod
    def _validate_age(age: int) -> int:
        if 0 < age <= 100:
            return(age)
        raise Exception('Возраст должен быть от 1 до 100.')


    def __str__(self) -> str:
        return f'{self._name}, {self._age}'


class Pilot(Human):
    def __init__(self, name: str, age: int, health: int):
        super().__init__(name, age)
        self.__health = health

    def is_helth(self):
        if self.__health < 10:
            return False

    def __str__(self) -> str:
        return f'{self._name}, {self._age}, {self.__health}'

people1 = Pilot('alex', 25, 5)
print(people1,)
people2 = Human('Ivan', 19)
print(people2)