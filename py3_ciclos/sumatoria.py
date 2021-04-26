A=[2,3,4,6]
B=[2,1,5,7]
C=[2,6,8,3]

def sumatoria_1(A,B,C):

  n=len(A)//2
  acumulador=0
  for i in range(n+1):
      d=A[i]*B[i]
      e=d+C[i]
      acumulador=acumulador + e
  resul = acumulador +(n**2)
  print(resul)
  return resul

sumatoria_1(A,B,C)


