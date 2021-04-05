
# Project Euler: 27
"""
Euler discovered the remarkable quadratic formula:

n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0<=n<=39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2-79n+1601 was discovered, which produces 80 primes for the consecutive values 0<=n<=79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|<=1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |-4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

import time

def euler_27(lim):

  primes1000 = get_primes(lim)

  primes = primes1000[:]  #copy of primes1000 variable

  largest = 0
  aa = bb = 0

  #looping through a quadratic equation
  for b in primes1000:
    for a in primes1000:
      i = 0
      #positive a and b
      while True:
        quadratic = i**2+a*i+b
        if quadratic not in primes:
          if is_prime(quadratic):
            primes.append(quadratic)
          else:
            if i-1 > largest:
              largest = i-1
              axb = a*b
              aa = a
              bb = b
            break
        i += 1
      i = 0
      #negative a and positive b
      while True:
        quadratic = i**2-a*i+b
        if quadratic not in primes:
          if is_prime(quadratic) and quadratic>0:
            primes.append(quadratic)
          else:
            if i-1 > largest:
              largest = i-1
              axb = -1*a*b
              aa = -a
              bb = b
            break
        i += 1

  return aa,bb,axb




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
  
  start = time.time()

  lim = 1000
  a,b,c = euler_27(lim)

  print("{} x {} = {}".format(a,b,c))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
-61 x 971 = -59231

Tiempo de operación: 1.8087048530578613 seg.
"""