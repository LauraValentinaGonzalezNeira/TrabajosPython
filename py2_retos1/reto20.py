
def bisiesto(año):
 cua=año%4
 cien=año%100
 cuatro=año%400
 if cua==0:
   if cien==0:
     if cuatro==0:
      print("El año es bisiesto")
     else:
      print("El año no es bisiesto")
   else:
     print("El año es bisiesto")
 else:
  print("El año no es bisiesto")

bisiesto(1985)