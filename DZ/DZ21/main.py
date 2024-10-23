
### Задача: Система управления курсами и студентами
# Описание: Разработайте систему управления курсами в университете. В системе могут быть курсы, студенты и преподаватели.
#  Студенты могут записываться на курсы, просматривать свои оценки и получать уведомления о новых заданиях. Преподаватели могут добавлять задания, выставлять оценки и отправлять уведомления. Курсы могут содержать несколько заданий, каждое из которых имеет максимальный балл.

# Дорабатываем задачу


from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, person_id: int, name: str, email: str):
        self._person_id: int = person_id
        self._name: str = name
        self._email: str = email

    @staticmethod
    @abstractmethod
    def from_console() -> 'Person':
        raise NotImplementedError('нужно реализовать метод')

    def __str__(self) -> str:
        return f'{self._person_id}: {self._name} ({self._email})'


class Teacher(Person):
    def __init__(self, person_id: int, name: str, email: str, job_title: str):
        super().__init__(person_id, name, email)
        self._job_title: str = job_title

    @staticmethod
    def from_console() -> 'Teacher':
        person_id: int = int(input('Введите id: '))
        name: str = input('Введите имя: ')
        email: str = input('Введите email: ')
        job_title: str = input('Введите должность: ')
        return Teacher(person_id, name, email, job_title)


class Student(Person):
    def __init__(self, person_id: int, name: str, email: str, grade: float):
        super().__init__(person_id, name, email)
        self._grade = grade

    @staticmethod
    def from_console() -> 'Student':
        person_id: int = int(input('Введите id: '))
        name: str = input('Введите имя: ')
        email: str = input('Введите email: ')
        grade: float = float(input('Введите оценку: '))
        return Student(person_id, name, email, grade)


class Course:
    def __init__(self, course_id: int, title: str):
        self._course_id: int = course_id
        self._title: str = title
        self._students: list[Student] = []

    def enroll(self, student: Student):
        self._students.append(student)

    def __str__(self) -> str:
        return f'Курс {self._title} (ID: {self._course_id})'


class University:
    def __init__(self):
        self.__teachers: list[Teacher] = []
        self.__courses: list[Course] = []
        self.__students: list[Student] = []

    def add_person(self, person: Person):
        if isinstance(person, Student):
            self.__students.append(person)
        elif isinstance(person, Teacher):
            self.__teachers.append(person)
        else:
            raise Exception('Можно добавить только студента или преподавателя')

    def add_course(self, course: Course):
        self.__courses.append(course)

    def enroll_student(self, course_id: int, student_id: int):
        course = next((c for c in self.__courses if c._course_id == course_id), None)
        student = next((s for s in self.__students if s._person_id == student_id), None)

        if course and student:
            course.enroll(student)
            print(f'Студент {student._name} зачислен на курс {course._title}.')
        else:
            print('Курс или студент не найдены.')

    def show_courses(self):
        for course in self.__courses:
            print(course)


# Тестируем систему
u = University()
u.add_person(Student(1, 'Андрюха', 'andrey@mail.ru', 5))
u.add_person(Teacher(2, 'Виктор Петрович', '2550033@mail.ru', 'Декан'))

# Добавление курсов
course1 = Course(101, 'Математика')
u.add_course(course1)

# Ввод через консоль
u.add_person(Teacher.from_console())
u.add_person(Student.from_console())

# Запись студента на курс
u.enroll_student(101, 1)

# Показать курсы
u.show_courses()