archivo = open('palabras500.csv', encoding= "utf-8")
lineas = archivo.readlines()
archivo.close()
num = input ("Ingrese las silabas que quiere ver: ")
def rima(num):
 m=len(num)
 for contador in lineas :
   x = contador
   y = x
   if num in y[-(m+1):]:
     print(x)

rima(num)