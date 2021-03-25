

# Project Euler: 31
"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
"""
200
100+100
100+50+50
100+50+20+20+10
100+50+20+20+5+5
etc
"""

import time

def euler_31(coins,target):

  ways = [1] + [0]*target
  
  for coin in coins:
      for i in range(coin, target+1):
          ways[i] += ways[i-coin]

  return ways[-1]

##############################################

if __name__ == "__main__":

  start=time.time()
  coins = [1,2,5,10,20,50,100,200]
  valor = 200

  c = euler_31(coins,valor)

  print("La cantidad de combinaciones es: {}".format(c))

  print("\n\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La cantidad de combinaciones es: 73682

Tiempo de operación: 0.002010822296142578 seg.
"""
