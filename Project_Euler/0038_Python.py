



# Project Euler: 38
"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
"""
- Para que el numero final empiece con 9 si o si el número debe empezar con 9.
- Si el número es 91 u 98     ->  Tenemos 8 digitos u 10
- Si el número es 912 u 987   ->  Tenemos 7 digitos u 11
- Si el número es 9123 u 9876 ->  Tenemos 9 digitos...OK!!
"""

import time

def euler_38(lim):
  ret = 0
  val = 0
  for valor in range(lim[0],lim[1]+1):
    if ''.join(sorted(str(valor)+str(valor*2))) == '123456789':
      if ret < int(str(valor)+str(valor*2)):
        ret = int(str(valor)+str(valor*2))
        val = valor
  return ret,val,[1,2]


##############################################

if __name__ == "__main__":
  
  start = time.time()
  
  lim = [9123,9876]

  n, number, lista = euler_38(lim)

  print("El numero es {} y esta formado por el valor {} multiplicado por {}".format(n,number,lista))

  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
El numero es 932718654 y esta formado por el valor 9327 multiplicado por [1, 2]

Tiempo de operación: 0.009956836700439453 seg.
"""


