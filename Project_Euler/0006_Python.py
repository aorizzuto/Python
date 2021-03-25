# Project Euler: 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def euler_6(n): 
  lst = list(range(1,n+1))
  a = sum([i**2 for i in lst])
  b = sum(lst)**2
  c = abs(a-b)
  return a,b,c


##############################################

if __name__ == "__main__":
  a,b,c = euler_6(100)
  print("Suma de cuadrados:\t\t{}\nCuadrado de la suma:\t{}\nDiferencia entre ambos:\t{}".format(a,b,c))
    
##############################################

"""
Suma de cuadrados:      338350
Cuadrado de la suma:    25502500
Diferencia entre ambos: 25164150
"""
