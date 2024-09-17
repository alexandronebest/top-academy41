# Модуль 5, часть 2, задание 1
# Напишите информационную систему «Сотрудники». 
# Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника, поиск 
# сотрудника по фамилии, вывод информации обо всех 
# сотрудниках, указанного возраста, или фамилия которых 
# начинается на указанную букву. Организуйте возможность 
# сохранения найденной информации в файл. Также весь 
# список сотрудников сохраняется в файл (при выходе из 
# программы — автоматически, в процессе исполнения 
# программы — по команде пользователя). При старте 
# программы происходит загрузка списка сотрудников из 
# указанного пользователем файла.




class Employee:
    def __init__(self, employee_id, name, surname, age):
        self.id = employee_id
        self.name = name
        self.surname = surname
        self.age = age

    def print_employee(self):
        print(f'№ сотрудника {self.id}')
        print(f'Имя сотрудника: {self.name}')
        print(f'Фамилия сотрудника: {self.surname}')
        print(f'Возраст сотрудника: {self.age}')

class EmployeeSystem:
    def __init__(self, filename):
        self.employees = []
        self.filename = filename
        self.load_employees()

    def load_employees(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    employee_id, name, surname, age = line.strip().split(',')
                    self.employees.append(Employee(int(employee_id), name, surname, age))
        except FileNotFoundError:
            print("Файл не найден, начнем с пустого списка.")

    def save_employees(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            for emp in self.employees:
                file.write(f'{emp.id},{emp.name},{emp.surname},{emp.age}\n')

    def add_employee(self):
        employee_id = len(self.employees) + 1
        name = input('Введите имя сотрудника: ')
        surname = input('Введите фамилию сотрудника: ')
        age = input('Введите возраст сотрудника: ')
        new_employee = Employee(employee_id, name, surname, age)
        self.employees.append(new_employee)

    def edit_employee(self):
        emp_id = int(input('Введите номер сотрудника для редактирования: '))
        for emp in self.employees:
            if emp.id == emp_id:
                emp.name = input('Введите новое имя сотрудника: ')
                emp.surname = input('Введите новую фамилию сотрудника: ')
                emp.age = input('Введите новый возраст сотрудника: ')
                return
        print("Сотрудник не найден.")

    def delete_employee(self):
        emp_id = int(input('Введите номер сотрудника для удаления: '))
        self.employees = [emp for emp in self.employees if emp.id != emp_id]

    def find_employee_by_surname(self):
        surname = input('Введите фамилию для поиска: ')
        for emp in self.employees:
            if emp.surname.lower().startswith(surname.lower()):
                emp.print_employee()

    def find_employees_by_age(self):
        age = input('Введите возраст для поиска: ')
        for emp in self.employees:
            if emp.age == age:
                emp.print_employee()

    def list_all_employees(self):
        for emp in self.employees:
            emp.print_employee()

    def main_menu(self):
        while True:
            print("\\n1. Добавить сотрудника")
            print("2. Редактировать сотрудника")
            print("3. Удалить сотрудника")
            print("4. Найти сотрудника по фамилии")
            print("5. Найти сотрудников по возрасту")
            print("6. Вывести всех сотрудников")
            print("7. Сохранить список сотрудников")
            print("8. Выход")
            choice = input("Выберите действие: ")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.edit_employee()
            elif choice == '3':
                self.delete_employee()
            elif choice == '4':
                self.find_employee_by_surname()
            elif choice == '5':
                self.find_employees_by_age()
            elif choice == '6':
                self.list_all_employees()
            elif choice == '7':
                self.save_employees()
                print("Список сотрудников сохранен.")
            elif choice == '8':
                self.save_employees()
                print("Выход из программы.")
                break
            else:
                print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    filename = input("Введите имя файла для загрузки сотрудников: ")
    employee_system = EmployeeSystem(filename)
    employee_system.main_menu()
    


