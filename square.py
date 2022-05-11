# квадрат
squarex = '0123456789'
squarey = '0123456789'
b = input('Введіть довжину сторони квадрвта (від 1 до 10): ')
x = squarex[0:int(b)]
y = x
for numeric in x:
  for num in y:
    place(-int(numeric), 0, num)