


# Project Euler: 47
"""
The first two consecutive numbers to have two distinct prime factors are:
14 = 2 x 7
15 = 3 x 5
The first three consecutive numbers to have three distinct prime factors are:
644 = 2^2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.
Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import time

def euler_47(num):

  while True:
    if prime_factors(num) == 4:
      num += 1
      if prime_factors(num) == 4:
        num += 1
        if prime_factors(num) == 4:
          num += 1
          if prime_factors(num) == 4:
            break
    num+=1

  return num - 3


def prime_factors(n):
  """function which will return
  the number of prime factors"""
  i = 2
  a = set()
  while i < n**0.5 or n == 1:
    if n % i == 0:
      n = n/i
      a.add(i)
      i -= 1
    i += 1
  return (len(a)+1)

##############################################

if __name__ == "__main__":

  start=time.time()
  valor = 1000

  c = euler_47(valor)

  print("El primer numero es: {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
El primer numero es: 134043

Tiempo de operación: 15.235317945480347 seg.
"""
