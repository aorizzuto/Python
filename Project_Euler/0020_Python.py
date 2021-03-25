


# Project Euler: 20
# Find the sum of the digits in the number 100!

import time

def euler_20(n): 
  cant = 1
  for i in range(n,1,-1):
    cant*=i
  
  ret=0
  for i in yield_sum(str(cant)):
    ret+=i
  return ret

def yield_sum(s):
  for i in s:
    yield int(i)

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 100

  a = euler_20(number)

  print("Suma de digitos del factorial de {}:\t{}".format(number,a))

  print("Tiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Suma de digitos del factorial de 100:   648
Tiempo de operación: 0.0004489421844482422 seg.
"""



