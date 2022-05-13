print('Вітаю Вас у лічільнику літер')
word = input('Введіть свій текст для підрахунку літер: ')
word = word.lower()
key_alpha = {
    'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'є': 0, 'ж': 0, 'з': 0, 'и': 0, 'і': 0,
    'ї': 0, 'й': 0, 'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0,
    'у': 0, 'ф': 0, 'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ь': 0, 'ю': 0, 'я': 0
}
for alpha in word:
    if alpha == 'а':
        key_alpha['а'] += 1
    elif alpha == 'б':
        key_alpha['б'] += 1
    elif alpha == 'в':
        key_alpha['в'] += 1
    elif alpha == 'г':
        key_alpha['г'] += 1
    elif alpha == 'д':
        key_alpha['д'] += 1
    elif alpha == 'е':
        key_alpha['е'] += 1
    elif alpha == 'є':
        key_alpha['є'] += 1
    elif alpha == 'ж':
        key_alpha['ж'] += 1
    elif alpha == 'з':
        key_alpha['з'] += 1
    elif alpha == 'и':
        key_alpha['и'] += 1
    elif alpha == 'і':
        key_alpha['і'] += 1
    elif alpha == 'ї':
        key_alpha['ї'] += 1
    elif alpha == 'й':
        key_alpha['й'] += 1
    elif alpha == 'к':
        key_alpha['к'] += 1
    elif alpha == 'л':
        key_alpha['л'] += 1
    elif alpha == 'м':
        key_alpha['м'] += 1
    elif alpha == 'н':
        key_alpha['н'] += 1
    elif alpha == 'о':
        key_alpha['о'] += 1
    elif alpha == 'п':
        key_alpha['п'] += 1
    elif alpha == 'р':
        key_alpha['р'] += 1
    elif alpha == 'с':
        key_alpha['с'] += 1
    elif alpha == 'т':
        key_alpha['т'] += 1
    elif alpha == 'у':
        key_alpha['у'] += 1
    elif alpha == 'ф':
        key_alpha['ф'] += 1
    elif alpha == 'х':
        key_alpha['х'] += 1
    elif alpha == 'ц':
        key_alpha['ц'] += 1
    elif alpha == 'ч':
        key_alpha['ч'] += 1
    elif alpha == 'ш':
        key_alpha['ш'] += 1
    elif alpha == 'щ':
        key_alpha['щ'] += 1
    elif alpha == 'ь':
        key_alpha['ь'] += 1
    elif alpha == 'ю':
        key_alpha['ю'] += 1
    elif alpha == 'я':
        key_alpha['я'] += 1
print(key_alpha)