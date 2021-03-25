



# Project Euler: 58
"""
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ˜ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

import time

def euler_58():
  
  x = 1
  step = 0
  contador_primos = 0

  while True:
    step += 2 # 2,4,6,8,10,12,14...

    for i in range(4):      
      x += step 
      
      if is_prime(x):
        contador_primos += 1

    if contador_primos / (step*2+1) < 0.1:
      break
    
  return step+1



def is_prime(n):
	"""function to check if the number is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True


##############################################

if __name__ == "__main__":

  start=time.time()

  c = euler_58()

  print("La cantidad es {}".format(c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La cantidad es 26241

Tiempo de operación: 32.56969714164734 seg
"""

