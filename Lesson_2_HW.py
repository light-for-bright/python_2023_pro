# 1 Вычисление площади круга:

radius = 5

def calculate_area():
    global radius
    area = 3.14 * radius ** 2
    return area

result = calculate_area()
print(f"Площадь круга с радиусом {radius} равна {result}")

# 2 Работа с локальными и глобальными переменными:
global_variable = 10

def modify_variable(local_variable):
    global global_variable
    local_variable += 5
    global_variable += 10
    return local_variable

local_variable = 7
modified_local = modify_variable(local_variable)
print(f"Локальная переменная: {local_variable}")
print(f"Глобальная переменная: {global_variable}")

# 3 Счетчик букв в строке:
def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

text = "Python - это забавно!"
letter_to_count = "а"
letter_count = count_letters(text, letter_to_count)
print(f"Буква '{letter_to_count}' встречается {letter_count} раз.")
