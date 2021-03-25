


# Project Euler: 46
"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9  = 7  + 2×1**2
15 = 7  + 2×2**2
21 = 3  + 2×3**2
25 = 7  + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

"""
Verificar de empezar con numeros altos y sumarle x**2 bajos
"""

import time

def euler_46(num):

  primes = get_primes(num)
  ret = -1
  for prime,isprime in enumerate(primes):
    if not isprime and prime >=9 and prime%2 == 1 and check_if_posible(prime,primes):
      continue
    else:
      if prime < 9 or isprime or prime%2 == 0:
        continue
    ret = prime
    break

  return ret





def check_if_posible(odd,primes):
  x = 1
  ret = False
  done = False

  while not done:
    for prime,isprime in enumerate(primes):
      if isprime:
        if odd == 5777:
          print(odd,prime,x,odd == (prime + 2*x**2))
        if odd == (prime + 2*x**2):
          ret = True
          done = True
          break
    x += 1

    if x>40:
      break

  return ret





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

  num = euler_46(n)

  print("El valor es: {}".format(num))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
El valor es: 5777

Tiempo de operación: 36.882713317871094 seg.
"""



