print('Вітаю, це конвертер системи числення з базою 18 у базу 10.')
print('Символи та їх значення:')
ind = '0123456789ABCDEFGH'
b = 18


for line in ind:
    print(f'{line} = {ind.find(line)}')
system = input('Введіть число використовуючи дану систему числення: ')
result = 0
for p, n in enumerate(reversed(system)):
    if n.isdigit():
        f = int(n)
    elif 9 < ord(n) - (ord('A') - 10) < b:
        f = ord(n) - (ord('A') - 10)
    else:
        print('Помилка')
        break

    result += f * b ** p
print(result)

