

# Project Euler: 21
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time

def euler_21(low,high): 
  L = [sum_divisors(i) for i in range(low,high + 1)]

  pairs = []

  for i in range(high - low + 1):
      ind = L[i]
      if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
          pairs.append([i+low,ind])
  return pairs

def sum_divisors(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s += i
    return s

def find_sum_divisors(pairs):
  return sum([sum(pair) for pair in pairs])

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 10000

  a = find_sum_divisors(euler_21(1,number))

  print("Suma de los numeros \"amicables\":\t{}".format(a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Suma de los numeros "amicables":    31626

Tiempo de operación: 12.402005672454834 seg.
"""


