# Project Euler: 10
# Find the sum of all the primes below two million.

def euler_10(n):
    multiples = set()

    for i in range(2, n+1):
        if i not in multiples:
            yield i # Primo
            multiples.update(range(i*i, n+1, i)) # Agrego multiplos del valor encontrado

##############################################

if __name__ == "__main__":
	iter = 0
	ml = list(euler_10(2000000))

	for x in ml:
    		iter = int(x) + iter

	print(iter)

##############################################

"""
142913828922
"""
