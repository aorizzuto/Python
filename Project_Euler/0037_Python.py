


# Project Euler: 37
"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import time

def euler_37(x):
  primes = getPrimes(x) # Lista de primos
  pares_cinco=['0','2','4','6','8','5']
  contador = 0
  
  for index, isPrime in enumerate(primes):
    if (not isPrime) or any([i in str(primes[index]) for i in pares_cinco]):
        continue

    if istruncateprime(primes, index):
      contador += index

  return contador - 2 - 3 - 5 - 7 # Remove primes less than 10



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



def istruncateprime(primes, number):
  number = str(number)

  for i in range(len(number)):
    if not primes[int(number[0:i+1])]:
      return False
    if not primes[int(number[i:])]:
      return False
  return True

##############################################

if __name__ == "__main__":
  
  start = time.time()
  
  x = 1000000

  contador = euler_37(x)

  print("La suma de los palindromos es: {}".format(contador))

  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
La suma de los palindromos es: 748317

Tiempo de operación: 2.597673177719116 seg.
"""

