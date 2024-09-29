print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

# функция разворачиват число и воозвращает его
def get_reverse_num(num: int) -> int:
    return int(str(num)[::-1])

# функция складывает два числа и воозвращает результат
def get_sum_nums(num1: int, num2: int) -> int:
    return num1 + num2



def main():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    reverse_num1 = get_reverse_num(num1)
    reverse_num2 = get_reverse_num(num2)
    total_sum = get_sum_nums(reverse_num1, reverse_num2)
    reverse_total_sum = get_reverse_num(total_sum)
    print(f"\nПервое число наоборот: {reverse_num1}")
    print(f"Второе число наоборот: {reverse_num2}")
    print(f"\nСумма: {total_sum}")
    print(f"Сумма наоборот: {reverse_total_sum}")


main()
