A=[2,-1,3,4]
B=[0,5,-10,4]
C=[]
def lista_1(A,B):
  n=len(A)//2
  for i in range(n):
      d = (A[i+1])**2
      e = d * B[2*i]
      f = e + B[n+1]
      C.append(f)
  print(C)
  return C

lista_1(A,B)