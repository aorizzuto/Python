
# Project Euler: 16
"""
What is the sum of the digits of the number 2^1000?
"""

import time

def euler_16(num):
  
  x = str(2**num)

  suma=0
  for i in x:
    suma += int(i)

  return x,suma

if __name__ == "__main__":
  a = 1000

  start=time.time()
  
  num,suma = euler_16(a)
  print("2^{} = {}. Suma = {}".format(a,num,suma))
  print("\nTiempo de operación:",time.time()-start,"seg")

"""
2^1000 = 1071508607186267320948425049060001810561404811705533607443750388
3703510511249361224931983788156958581275946729175531468251871452856923140
4359845775746985748039345677748242309854210746050623711418779541821530464
7498358194126739876755916554394607706291457119647768654216766042983165262
4386837205668069376. Suma = 1366

Tiempo de operación: 0.0002543926239013672 seg
"""



