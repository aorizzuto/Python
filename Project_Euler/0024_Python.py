

# Project Euler: 24
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import time
from itertools import permutations

def euler_24(n): 
  perm = sorted(''.join(chars) for chars in permutations('0123456789'))

  return perm[n-1]

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 1000000

  a = euler_24(number)

  print("N° {} en permutaciones:\t{}".format(number,a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
N° 1000000 en permutaciones:    2783915460

Tiempo de operación: 4.333045959472656 seg.
"""


