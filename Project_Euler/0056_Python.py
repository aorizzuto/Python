


# Project Euler: 56
"""
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

import time

def euler_56(a,b):
  maximo = 0
  for i in range(a-1,1,-1):   # 99 a 1
    for j in range(b-1,1,-1): # 99 a 1
      suma = 0
      x = i**j
      for k in str(x):
        suma += int(k)
      
      maximo = max([maximo,suma])


  return maximo

##############################################

if __name__ == "__main__":

  start=time.time()

  a = 100
  b = 100
  c = euler_56(a,b)

  print("La suma máxima de digitos es {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La suma máxima de digitos es 972

Tiempo de operación: 0.677879810333252 seg.
"""

