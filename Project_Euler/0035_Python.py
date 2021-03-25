


# Project Euler: 35
"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
"""
Verificar hacer combinaciones de 1,3,7,9 de hasta 7 digitos y verificar que sean primos
"""

import time

def euler_35(x):
  primes = getPrimes(x) # Lista de primos
  pares_cinco=['0','2','4','6','8','5']
  contador = 0
  
  for index, isPrime in enumerate(primes):
      if (not isPrime) or any([i in str(primes[index]) for i in pares_cinco]):
          continue
      if isCircularPrime(primes, index):
          contador += 1

  return contador

def getPrimes(n=100):

  primes = [True] * n   # Genero lista toda en True
  primes[0] = False     # 0 no es Primo
  primes[1] = False     # 1 no es Primo

  for number in range(2, n): # Por cada número entre 2 y 999.999
      if not primes[number]: # Si está en False es porque es multiplo de algun primo anterior
          continue

      # Y pongo en False a los múltiplos
      for index in range(number*2, n, number):
          primes[index] = False

  return primes


def isCircularPrime(primes, number):
    number = str(number)
    for i in range(len(number)):
        number = number[1:] + number[0]
        if not primes[int(number)]:
            return False
    return True

##############################################

if __name__ == "__main__":
  start = time.time()
  
  x = 1000000
  
  contador = euler_35(x)

  print("La cantidad de primos circulares menores a {} son: {}".format(x,contador))

  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
La cantidad de primos circulares menores a 1000000 son: 55

Tiempo de operación: 2.580852508544922 seg.
"""


