

# Project Euler: 49
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import time
from itertools import permutations

def euler_49(n):

  primes = get_primes(n)

  done = False

  for x in range(1000,len(primes)):
    if x not in [1487,4817,8147]:
      for z in range(len(primes)-1,0,-1):
        if primes[x] and primes[z] and (z-x)%2 == 0 and x!=z:
          y = int(x+(z-x)/2)
          if primes[y]:
            if are_permutations(str(x),str(y),str(z)):
              done = True
              break
    if done:
      break
  print(x,y,z)
  return str(x)+str(y)+str(z)



def are_permutations(x,y,z):
  return sorted(list(x)) == sorted(list(y)) == sorted(list(z))



def get_primes(n):
  primes = [True] * n   # Genero lista toda en True
  primes[0] = False     # 0 no es Primo
  primes[1] = False     # 1 no es Primo

  for number in range(2, n): # Por cada número entre 2 y sup

    if not primes[number]: # Si está en False es porque es multiplo de algun primo anterior
      continue

    # Y pongo en False a los múltiplos
    for index in range(number*2, n, number):
      primes[index] = False

  return primes






##############################################

if __name__ == "__main__":
  
  start = time.time()

  n = 10000

  num = euler_49(n)

  print("El valor concatenado es: {}".format(num))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
2969 6299 9629
El valor concatenado es: 296962999629

Tiempo de operación: 5.803735733032227 seg
"""

