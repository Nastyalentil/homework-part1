print('Вітаю Вас у лічільнику літер')
word = input('Введіть свій текст для підрахунку літер: ')

key_count = {}
for alpha in word:
    if alpha in key_count:
        key_count[alpha] += 1
    else:
        key_count[alpha] = 1
print(key_count)