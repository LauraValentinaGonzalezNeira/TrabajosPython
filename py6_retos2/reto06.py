import random
numero =random.randint(1,120)
print(numero)
if numero > 9 and numero < 51:
  print('El número esta entre 10 y 50')
elif numero > 50 and numero < 101:
  print('El número esta entre 51 y 100')
elif numero > 100:
  print('El número es mayor a 100')
elif numero < 10:
  print('El número es menor a 10')