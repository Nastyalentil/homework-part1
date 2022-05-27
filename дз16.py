print('Вітаю!')


def input_cucumber():

    cucumber = input('Введіть будьласка "Cucumber": ')

    cucumberind = cucumber[1:]

    assert cucumber.istitle(), 'Виникла помилка, слово починається з маленької літери, будь ласка, спробуйте ще раз.'
    assert cucumberind.islower(), 'Виникла помилка, здається є великі літери окрім першої, будь ласка, перевірте та спробуйте ще раз.'
    assert ' ' not in cucumber, 'Виникла помилка, перевірте, чи немає зайвих пробілів у тексті та спробуйте ще раз.'
    assert cucumber == 'Cucumber', 'Виникла помилка, здається це не слово "Cucumber", будь ласка, спробуйте ще раз.'

    return(cucumber)

try:
    cucumber = input_cucumber()
    print('Дякую, все вірно!')
except AssertionError as error:
    print(error)
    input_cucumber()


