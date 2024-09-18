# Задание 4
# Создайте класс «Дробь». Необходимо хранить в полях
# класса: числитель и знаменатель. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к
# отдельным полям через методы класса. Также создайте
# методы класса для выполнения арифметических операций
# (сложение, вычитание, умножение, деление, и т.д.).

from __future__ import annotations


class Fraction:
	def __init__(self, numerator: int, denominator: int, int_part: int = 0):
		self.__num: int = numerator + int_part * denominator
		self.__den: int = denominator

	# @property
	# def num(self) -> int:
	# 	return self.__num
	#
	# @num.setter
	# def num(self, value):
	# 	if type(value) == int:
	# 		self.__num = value

	def add(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__den + fraction.__num * self.__den
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def multiply(self, fraction: Fraction) -> Fraction:
		num = self.__num * fraction.__num
		den = self.__den * fraction.__den
		return Fraction(num, den)

	def __str__(self) -> str:
		num = self.__num

		if self.__num > self.__den:
			int_part = int(self.__num / self.__den)
			num -= int_part * self.__den
			return f'{int_part} ({num}/{self.__den})'
		elif self.__num == self.__den:
			return str(int(self.__num / self.__den))

		return f'{self.__num}/{self.__den}'

	def __float__(self):
		return self.__num / self.__den


# f1 = Fraction(2, 3, int_part=3)
f2 = Fraction(555, 40)
#
# f3: Fraction = f1.add(f2)
# f4: Fraction = f3.add(f1)

print(f2)
# print(f.get_num())