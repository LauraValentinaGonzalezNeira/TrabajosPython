casillas = 64
granos=0
for i in range(casillas):
 granos=2**i+granos
print('Se necesitan', granos, 'granos de trigo')
