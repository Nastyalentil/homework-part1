print('Вітаю! Це шифрувальник для шифру Цезаря.\n(Алфавіт - англійський)')

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
text = input('Введіть текст для шифрування: ')
key = int(input('Введіть ключ від 1 до 25: '))
text2 = ''
for letter in text:
    position = alphabet.find(letter)
    newposition = position + key
    if letter in alphabet:
        text2 = text2 + alphabet[newposition]
    else:
        text2 = text2 + letter
print(text2)