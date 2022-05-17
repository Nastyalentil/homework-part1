# name = input("Введіть ваше імя: ")
# print("Вітаю", name + "!")
choose = input('Оберіть вид операції (*,+,-,/,+++): ')
if choose == "+++":
    num = []
    number = []
    while number != 0:
        number = int(input('Введіть числа, які хочете просумувати(якщо хочете завершити введіть "0"): '))
        num.append(number)
        nums = sum(num)
    print(nums)

else:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))

    if choose == "*":
        a = number1 * number2
        print(a)
    elif choose == "+":
        b = number1 + number2
        print(b)
    elif choose == '-':
        c = number1 - number2
        print(c)
    elif choose == '/':
        try:
            d = number1 / number2
        except ZeroDivisionError:
            d = ('inf')
        print(d)
    else:
        print("Помилка!")