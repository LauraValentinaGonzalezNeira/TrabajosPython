import matplotlib.pyplot as plt
lista = []
num= input ("Ingrese el número que deseé")
type(int(num))
while num != 1:
  if num %2 == 0:
    num = num/2
    lista.append(num) 
  else:
    num = (num*3)+1
    lista.append(num)
print(lista)
