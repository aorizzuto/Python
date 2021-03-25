





# Project Euler: 53
"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (5/3)=10.

In general, (n/r)=n!/r!(n-r)!, where r<=n, n!=n×(n-1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (23/10)=1144066.

How many, not necessarily distinct, values of (n/r) for 1<=n<=100, are greater than one-million?
"""

import time

def euler_53(num, millon):

  cant = 0
  
  for n in range(1,num+1):
    for r in range(1,n):
      res = get_result(n,r)

      if res >= millon:
        cant += 1
      
  return cant

def get_result(n,r):
  return fact(n)/(fact(r)*fact(n-r))

def fact(n):
  num = 1
  while n != 1:
    num *= n
    n -= 1
  
  return num



##############################################

if __name__ == "__main__":

  start=time.time()
  valor = 100
  millon = 1000000

  c = euler_53(valor,millon)

  print("Los valores son: {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Los valores son: 4075

Tiempo de operación: 0.26448702812194824 seg.
"""

