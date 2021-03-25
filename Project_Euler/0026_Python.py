


# Project Euler: 26
"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/6	= 	0.1(6)
1/7	= 	0.(142857)

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

import time

def euler_26(n):
  decimales = [] 
  ciclos = []

  for i in range(2,n+1):
    num = 10**len(str(i))
    original = num
    decimales.clear()
    while True:
      resto = num % i

      if resto == 0:
        ciclos.append('')
        break
      elif str(num//i) in decimales and str(num//i) != '0':
        ciclos.append(''.join(decimales[decimales.index(str(num//i)):]))
        break
      
      decimales.append(str(num//i))
      num = resto*(10**len(str(i)))

  maximo = 0
  for i in range(len(ciclos)):
    if len(str(ciclos[i])) > maximo:
      maximo = len(str(ciclos[i]))
      item = i+2

  return item

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 1000

  a = euler_26(number)

  print("1/{} tiene el mayor ciclo periódico".format(a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
1/983 tiene el mayor ciclo periódico

Tiempo de operación: 1.2398431301116943 seg.
"""


