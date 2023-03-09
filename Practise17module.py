import bisect
# модуль bisect использую, чтобы вызвать функцию bisect.bisect_left
# которая обеспечивает поддержку вставки значений в отсортированный список, без необходимости сортировать этот список
# после каждой вставки, своего рода оптимизация кода

def binary_search(sorted_list, item):  # Реализация алгоритма двоичного поиска
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return low


numbers_input = input("Введите последовательность чисел через пробел: ")
try:
    numbers = [float(x) for x in
               numbers_input.split()]  # использую float поскольку в задаче указано, что может быть ЛЮБОЕ число,
    # соответственно с плавающей точкой
except ValueError:
    print("Ошибка ввода: в последовательности должны быть только числа")
    exit()

number_input = input("Введите любое число: ")
try:
    number = float(number_input)
except ValueError:
    print("Ошибка ввода: вы ввели не число")
    exit()

numbers.sort()

position = bisect.bisect_left(numbers, number)
if position == 0 or position == len(numbers) - 1:
    print(f"Введенное число {number} — не подходит по условию задачи")
else:
    print(f"Позиция элемента числа {number} находится между индексами {position - 1} и {position} чисел {numbers[position - 1]} и {numbers[position]}")
