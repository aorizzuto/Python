

# Project Euler: 52
"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import time

def euler_52(num):

  for i in range(num,num*10):
    if check_digits(i,2*i):
      if check_digits(i,3*i):
        if check_digits(i,4*i):
          if check_digits(i,5*i):
            if check_digits(i,6*i):
              break
      
  return i


def check_digits(a,b):
  return len(str(a)) == len(str(b)) and sorted(set(str(a)))==sorted(set(str(b)))



##############################################

if __name__ == "__main__":

  start=time.time()
  valor = 100000

  c = euler_52(valor)

  print("Los valores son: {} - {} - {} - {} - {} - {}".format(c,c*2,c*3,c*4,c*5,c*6))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Los valores son: 142857 - 285714 - 428571 - 571428 - 714285 - 857142

Tiempo de operación: 0.5491280555725098 seg.
"""
