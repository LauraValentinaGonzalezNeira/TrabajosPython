A=[2,3,4]
B=[3,6,5]
C=[2,7,6]

n=len(A)

X=sum(((A[i]*B[i])+C[i]) for i in range(n))+n**2
print(X)
