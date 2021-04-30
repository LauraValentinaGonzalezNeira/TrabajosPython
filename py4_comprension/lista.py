A=[2,5,6,4]
B=[2,3,6,5]

n=len(A)//2

C=[(((A[i+1])**2)*B[2*i])+B[n+i] for i in range(n) ]
print(C)