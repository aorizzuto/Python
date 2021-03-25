


# Project Euler: 57
"""
Too much special characters
"""
"""
1,1
3/2 = 1+2*1 / 1+1
7/5 = 3*2*2 / 3+2
17/12 = 7+2*5 / 7+5
41/29 = 17+2*12 / 17+12
99/70 = 41+2*29 / 41+29
...
n/m = (n-1)+2*(m-1) / (n-1)+(m-1)
"""

import time

def euler_57(a,b):
  
  cant = 0
  x = 1 # Numerator
  y = 1 # Denominator
  for num in range(1,b+1):
    x0 = x
    x = x+a*y
    y = x0+y

    if len(str(x)) > len(str(y)):
      cant += 1
    

  return cant

##############################################

if __name__ == "__main__":

  start=time.time()

  a = 2
  b = 1000
  c = euler_57(a,b)

  print("La cantidad es {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La cantidad es 153

Tiempo de operación: 0.0034384727478027344 seg.
"""


