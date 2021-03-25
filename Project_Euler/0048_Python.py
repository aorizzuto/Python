

# Project Euler: 48
"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

import time

def euler_48(num):

  suma = 0
  for i in yield_sum(num):
    suma += i

  return str(suma)


def yield_sum(n):
  for i in range(1,n+1):
    yield i**i




##############################################

if __name__ == "__main__":
  
  start = time.time()

  n = 1000
  dig = 10

  num = euler_48(n)

  print("Los ultimos {} digitos son: {}".format(dig,num[-dig:]))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
Los ultimos 10 digitos son: 9110846700

Tiempo de operación: 0.026721477508544922 seg.
"""


