



# Project Euler: 40
"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

import time

def euler_40(lim):
  num = 1   # Numero que aumentará hasta "lim"
  n = 0     # Numero que aumenta de 1 en 1
  cant = 1  # Aumento en 1 cada vez que pasa por 10,100,1000...
  cant2 = 1
  mul = 1

  while num<=lim:
    n += 1
    if n % (10**cant) == 0:
      cant += 1
    num +=cant
    
    
    if num >= (10**cant2):
      cant2 +=1
      mul *= int(str(n+1)[num - (10**cant)])

  return mul


##############################################

if __name__ == "__main__":
  
  start = time.time()
  
  lim = 1000000

  val = euler_40(lim)

  print("El valor es {}".format(val))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
El valor es 210

Tiempo de operación: 0.4113807678222656 seg.
"""

