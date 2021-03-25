
# Project Euler: 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from functools import reduce
from math import gcd

def euler_5(n): 
  return (reduce(lcm, range(1,n+1)))

def lcm(a,b):
  return a*b//gcd(a,b)    

##############################################

if __name__ == "__main__":
  a = euler_5(20)
  print("Min comun multiplo:",a)
    
##############################################

"""
Min comun multiplo: 232792560
"""
