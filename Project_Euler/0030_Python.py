

# Project Euler: 30
"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
"""
El máximo que podemos hacer es:
9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5 = 355000.
Este será nuestro limite superior
"""

import time

def euler_30(a,b):
  lim = 355000
  lst = []

  for i in range(2,lim+1):  # El 1 lo obvio
    suma = 0
    for j in str(i):
      suma = suma + int(j)**5

    if suma == i:
      lst.append(i) 

  return sum(lst)

##############################################

if __name__ == "__main__":

  start=time.time()
  a = 100 # Numero
  b = 100 # Potencia

  c = euler_30(a,b)

  print("La suma de los numeros es: {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La suma de los numeros es: 443839

Tiempo de operación: 4.562664031982422 seg.
"""


