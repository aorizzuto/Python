

# Project Euler: 32
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import time
from itertools import permutations

def euler_32(pan):
  total = []
  for i in yield_pan(pan):
    total.append(i)
  return sum(set(total))

def check_number(pan,i,j):
  s = str(i*j)+str(i)+str(j)
  return ''.join(sorted(list(s))) == pan

def yield_pan(pan):
  for k in range(4,2,-1):
    num1 = list(permutations(list(pan), k))
    for l in range(1,k+1):
      num2 = list(permutations(list(pan), l))

      for i in num1:
        i=int(''.join(i))
        for j in num2:
          j=int(''.join(j))

          if check_number(pan,i,j):
            yield i*j

##############################################

if __name__ == "__main__":

  start=time.time()
  pan = '123456789'

  c = euler_32(pan)

  print("La suma de los productos es: {}".format(c))

  print("\n\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La suma de los productos es: 45228


Tiempo de operación: 112.11005735397339 seg.
"""

