# Project Euler: 50
"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import time

def euler_50(num):

  primes = get_primes(num)

  cant = 0
  cantidad = 0
  longest=0
  suma = 0

  for i in range(len(primes)-1):
    suma += primes[i]
    cant += 1
    for j in range(i+1,len(primes)):
      suma += primes[j]
      cant += 1
      if is_prime(suma) and suma < num and cant > cantidad:
        longest = suma
        cantidad = cant
    suma = 0
    cant = 0
      

  return cantidad,longest


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




def is_prime(n):
	"""function to check if the number is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True


##############################################

if __name__ == "__main__":

  start=time.time()
  valor = 1000000

  a,c = euler_50(valor)

  print("La suma mas larga es {} y tiene {} numeros".format(c,a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""

"""