# Project Euler: 60
"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import time

def euler_60(lim):
  
  primes = get_primes(lim)
  
  return 0



def is_prime(n):
	"""function to check if the number is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True



def get_primes(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime




##############################################

if __name__ == "__main__":

  p = [3, 7, 109, 673]

  start=time.time()
  
  c = euler_60(lim)

  p.append(c)

  print("Los 5 primos con esta propiedad son: {}".format(p))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La cantidad es 153

Tiempo de operación: 0.0034384727478027344 seg.
"""