import random

def create_and_fill_array(size):
    # Создаем двумерный массив размерности size x size
    array = [[0.0] * size for _ in range(size)]

    # Заполняем массив случайными дробными числами в диапазоне 0.00 - 0.99
    for i in range(size):
        for j in range(size):
            array[i][j] = round(random.uniform(0.0, 0.99), 2)

    return array

def print_array(array):
    # Выводим массив на экран
    for row in array:
        for elem in row:
            print(elem, end='\t')
        print()

def find_min_diagonal_element(array):
    # Находим минимальный ненулевой элемент диагонали
    min_element = 0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i==j and (len(array)%2!=0):
                if array[i][j]>0 and array[i][j]<min_element:
                    min_element= array[i][j]


    return min_element

# Запрос числа у пользователя
while True:
    size = int(input("Введите число (больше трех и являющееся нечетным): "))
    if size > 3 and size % 2 != 0:
        break
    else:
        print("Некорректный ввод. Пожалуйста, введите число больше трех и нечетное.")

# Создаем и заполняем массив
matrix = create_and_fill_array(size)

# Выводим массив
print("Сгенерированный массив:")
print_array(matrix)

min = find_min_diagonal_element(matrix)

# Выводим результат
print(f"\nМинимальный ненулевой элемент диагонали: {min}")
