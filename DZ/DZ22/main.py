# Модуль 8, часть 1, задание 1
# Есть некоторый словарь, который хранит названия 
# стран и столиц. Название страны используется в качестве 
# ключа, название столицыв качестве значения. Необходимо 
# реализовать: добавление данных, удаление данных, поиск 
# данных, редактирование данных, сохранение и загрузку 
# данных (используя упаковку и распаковку).

import json

class CountryCapital:
    def __init__(self):
        self.data = {}

    def add_country(self, country, capital):
        self.data[country] = capital
        print(f"Добавлена страна: {country}, столица: {capital}")

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
            print(f"Страна: {country} удалена.")
        else:
            print(f"Страна: {country} не найдена.")

    def find_capital(self, country):
        capital = self.data.get(country)
        if capital:
            print(f"Столица страны: {country}: {capital}")
        else:
            print(f"Страна {country} не найдена.")

    def edit_country(self, country, new_country, new_capital):
        if country in self.data:
            del self.data[country]
            self.data[new_country] = new_capital
            print(f"Страна {country} изменена на {new_country}, столица: {new_capital}")
        else:
            print(f"Страна {country} не найдена.")

    def save_data(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)
            print(f"Данные сохранены в {filename}")

    def load_data(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                self.data = json.load(file)
                print(f"Данные загружены из {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")

# Пример использования
if __name__ == "__main__":
    country_capital_dict = CountryCapital()

    # Добавление данных
    country_capital_dict.add_country('Россия', 'Москва')
    country_capital_dict.add_country('Франция', 'Париж')

    # Поиск данных
    country_capital_dict.find_capital('Россия')
    country_capital_dict.find_capital('Италия')

    # Редактирование данных
    country_capital_dict.edit_country('Франция', 'Франция', 'Лион')

    # Удаление данных
    country_capital_dict.remove_country('Россия')

    # Сохранение данных
    country_capital_dict.save_data('countries.txt')

    # Загрузка данных
    country_capital_dict.load_data('countries.txt')

# Модуль 8, часть1, задание 2
# Есть некоторый словарь, который хранит названия 
# музыкальных групп(исполнителей) и альбомов. Название группы используется в качестве ключа, название 
# альбомов в качестве значения. Необходимо реализовать: 
# добавление данных, удаление данных, поиск данных, 
# редактирование данных, сохранение и загрузку данных 
# (используя упаковку и распаковку).

import json

class Music:
    def __init__(self):
        self.data = {}

    def add_music(self, group, album):
        if group in self.data:
            self.data[group].append(album)
        else:
            self.data[group] = [album]
        print(f"Добавлена группа: {group}, альбом: {album}")

    def remove_music(self, group):
        if group in self.data:
            del self.data[group]
            print(f"Группа: {group} удалена.")
        else:
            print(f'Группа {group}, не найдена')

    def find_album(self, group):
        albums = self.data.get(group)
        if albums:
            print(f"Альбомы группы {group}: {', '.join(albums)}")
        else:
            print(f"Группа {group} не найдена.")

    def edit_group(self, group, new_group, new_album):
        if group in self.data:
            del self.data[group]
            self.data[new_group] = [new_album]  # Создаем новый список для нового альбома
            print(f"Группа {group} изменена на {new_group}, альбом: {new_album}")
        else:
            print(f"Группа {group} не найдена.")

    def save_data(self, filename):
        if filename.endswith('.json'):
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(self.data, file, ensure_ascii=False, indent=4)
                print(f"Данные сохранены в {filename}")
        else:
            with open(filename, 'w', encoding='utf-8') as file:
                for group, albums in self.data.items():
                    file.write(f"{group}: {', '.join(albums)}\n")
                print(f"Данные сохранены в {filename}")

    def load_data(self, filename):
        try:
            if filename.endswith('.json'):
                with open(filename, 'r', encoding='utf-8') as file:
                    self.data = json.load(file)
                    print(f"Данные загружены из {filename}")
            else:
                with open(filename, 'r', encoding='utf-8') as file:
                    self.data = {}
                    for line in file:
                        group, albums = line.strip().split(': ')
                        self.data[group] = albums.split(', ')
                    print(f"Данные загружены из {filename}")
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")

# Пример
music_collection = Music()
music_collection.add_music("Centr", "Качели")
music_collection.add_music("Slipknot", "Lowa")
music_collection.find_album("Slipknot")
music_collection.edit_group("Centr", "AC/DC", "Highway to Hell")
music_collection.find_album("Slipknot")
music_collection.save_data("music_data.txt")
music_collection.load_data("music_data.txt")
music_collection.find_album("Slipknot")

music_collection.save_data("music_data.json")
music_collection.load_data("music_data.json")