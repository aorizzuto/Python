# Project Euler: 3
#    What is the largest prime factor of the number 600851475143 ?

def euler_3(n):
    
    num = n
    l = []
    
    while True:
        for i in range(7,num+1,2):
            if num % i == 0:
                if check_if_prime(i):
                    num //= i
                    l.append(i)
                    break
        if num == 1:
            break
    
    print("Prime numbers:",l)
    return l[-1]

def check_if_prime(n):
    
    return len([i for i in range(3,n,2) if n % i == 0]) == 0

##############################################

if __name__ == "__main__":
    print("Largest prime factor of 600851475143:",euler_3(600851475143))
    
##############################################

"""
[71, 839, 1471, 6857]
Largest prime factor of 600851475143: 6857
"""
