numbers_list = [10, 25, 52, 63, 217]
user_number = int(input("Угадай число: "))
if user_number in numbers_list:
    print("Исходный список:", numbers_list)
    print("Ваше число:", user_number)
    print("Поздравляю, Вы угадали число!")
else:
    print("Исходный список:", numbers_list)
    print("Ваше число:", user_number)
    print("Нет такого числа!")
