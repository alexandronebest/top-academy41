# Модуль 5, часть 1, задание 1
# Дано два текстовых файла. Выяснить, совпадают ли 
# их строки. Если нет, то вывести несовпадающую строку 
# из каждого файла.


# первый файл
with open('text1.txt', 'r', encoding='utf-8') as file1:
    lines1 = file1.readlines()  
# Второй файл
with open('text2.txt', 'r', encoding='utf-8') as file2:
    lines2 = file2.readlines()
    max_length = max(len(lines1), len(lines2))
lines1 += ['\\n'] * (max_length - len(lines1))  
lines2 += ['\\n'] * (max_length - len(lines2))
for i in range(max_length):
    if lines1[i] != lines2[i]:  
        print(f'Несовпадающая строка в text1.txt (строка {i + 1}): {lines1[i].rstrip()}')
        print(f'Несовпадающая строка в text2.txt (строка {i + 1}): {lines2[i].rstrip()}')

# Модуль 5, часть 1, задание 2
# Дан текстовый файл. Необходимо создать новый файл 
# и записать в него следующую статистику по исходному 
# файлу:
# ■ Количество символов;
# ■ Количество строк;
# ■ Количество гласных букв;
# ■ Количество согласных букв;
# ■ Количество цифр.

text: str = ''
simbol_count = 0
glas_count = 0
sogl_count = 0
num_count = 0
glas = ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")
sogl = ("б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ")

with open('input.txt', encoding='utf-8') as f:
    text = f.read()

# Подсчет символов
simbol_count = len(text)

# Подсчет строк
num_lines = text.count('\n') + 1 if text else 0
for char in text.lower():  # приводим к нижнему регистру 
    if char.isalpha():  # Проверяем если символ буква
        if char in glas:
            glas_count += 1
        elif char in sogl:
            sogl_count += 1
    elif char.isdigit():  #если символ цифра
        num_count += 1 
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f'Количество символов: {simbol_count}\n')
    f.write(f'Количество строк: {num_lines}\n')
    f.write(f'Количество гласных: {glas_count}\n')
    f.write(f'Количество согласных: {sogl_count}\n')
    f.write(f'Количество цифр: {num_count}\n')
    
# Модуль 5, часть 1, задание 3 
# Дан текстовый файл. Удалить из него последнюю 
# строку. Результат записать в другой файл.


with open('textindz3.txt', encoding='utf-8') as f:
    lines = f.readlines()
    lines = lines[:-1]  # Удаляем последнюю строку
with open('textoutdz3.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)  


# Модуль 5, часть 1, задание 4
# Дан текстовый файл. Найти длину самой длинной 
# строки.

with open('textdz4.txt', encoding='utf-8') as f:
    lines = f.readlines()
    max_lines = max(lines, key=len).strip()
    print(  f'Самая длинная строка: {max_lines}; под номером: {lines.index(max(lines, key=len))+1}')

    

# Модуль 5, часть 1, задание 5
# Дан текстовый файл. Посчитать сколько раз в нем 
# встречается заданное пользователем слово.

word_count = 0
with open('textdz5.txt', encoding='utf-8') as f:
    text = f.read()

word = input('Введите слово, которое хотите посчитать, например "привет": ')
res = text.split()
for i in res:
    # Удалим знаки и приведем к нижнему регистру(lower)
    cleaned_word = i.strip('.,!?\\";:()[]{}').lower()
    if cleaned_word == word.lower():  # Сравниваем (lower) в нижнем регистре
        word_count += 1
if word_count > 0:
    print(f'Слово "{word}" встречается {word_count} раз.')
else:
    print(f'Слово "{word}" не найдено в тексте.')

# Модуль 5, часть 1, задание 6
# Дан текстовый файл. Найти и заменить в нем заданное слово. Что искать и на что заменять определяется 
# пользователем.

word_replace = input('Введите слово, которое хотите заменить: ')
replace_word = input('Введите на что хотите его заменить: ')
with open('textdz6.txt', encoding='utf-8') as f:
    text = f.read()
# Заменяем  на новое значение
text = text.replace(word_replace, replace_word)
# Изменения обратно 
with open('textdz6.txt', 'w', encoding='utf-8') as f:
    f.write(text)
print('Заменено')
