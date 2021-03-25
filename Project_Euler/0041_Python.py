



# Project Euler: 41
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""
"""
9+8+7+6+5+4+3+2+1 = 45  -> Multiplo de 3  -> No pueden ser 9 digitos
8+7+6+5+4+3+2+1 = 36    -> Multplo de 3   -> No pueden ser 8 digitos
7+6+5+4+3+2+1 = 28      -> No es multiplo de 3
"""

import time

def euler_41(sup):

  primes = getPrimes(sup+1)

  while sup>0:
    if primes[sup] and is_pandigital(sup):
      break
    sup -= 2

  return sup


def is_pandigital(n):
  num = sorted(str(n))
  return num[0]!=0 and ''.join(num) == '1234567'[:len(num)]



def getPrimes(n):

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
  
  sup = 7654321

  val = euler_41(sup)

  print("El valor es {}".format(val))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
El valor es 7652413

Tiempo de operación: 14.470308780670166 seg.
"""



VER ESTA FORMA

# http://radiusofcircle.blogspot.com

# time module for calculating time
import time

#permutation method
from itertools import permutations

#time at the start of program execution
start = time.time()


def is_prime(n):
    """function to check if the given
    number is prime"""
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# starting with 1-9 digits
a = '123456789'

# flag to stop while loop when prime is found
flag = True

# while loop iterator
j = 9

# while loop
while flag:
    p = permutations(a[:j])
    p = list(p)[::-1]
    for i in p:
        if int(i[j-1]) % 2 != 0:
            number = int(''.join(i))
            if (number+1) % 6 == 0 or (number-1) % 6 == 0:
                if is_prime(number):
                    print(number)
                    flag = False
                    break
    j -= 1

# time at the end of program execution
end = time.time()

# total execution time
print(end - start)

