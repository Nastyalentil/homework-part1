import time
import random
name = input("Введіть ваше імя: ")
print("Вітаю", name + "!", "Зараз буде змійка ^_^")
time.sleep(1.5)


while True:
    try:
        star = ['*', '  *', ' *', '   *']
        stars = random.choice(star)
        print(stars)
        time.sleep(0.1)
    except :
        print('^_^')
        break