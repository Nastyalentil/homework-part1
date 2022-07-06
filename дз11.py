print('Вітаю! Це шифрувальник та дешифрувальник для шифру Цезаря.\n(Алфавіт - англійський)')

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

choice = int(input('Введіть "1" для шифрування або "2" для дешифрування: '))

if choice == 1:
    text = input('Введіть текст для шифрування: ')
    key = int(input('Введіть ключ від 1 до 25: '))
    text = text.lower()
    text2 = ''
    for letter in text:
        position = alphabet.find(letter)
        newposition = position + key
        if letter in alphabet:
            text2 = text2 + alphabet[newposition]
        else:
            text2 = text2 + letter
    print(text2)
elif choice == 2:
    text = input('Введіть текст для шифрування: ')
    key = int(input('Введіть ключ від 1 до 25: '))
    text = text.lower()
    text2 = ''
    for letter in text:
        position = alphabet.find(letter)
        newposition = position - key
        if letter in alphabet:
            text2 = text2 + alphabet[newposition]
        else:
            text2 = text2 + letter
    print(text2)
