
# Project Euler: 12
# What is the value of the first triangle number to have over five hundred divisors?

import math

def euler_12(n):

  for value in gen():
    if sum(2 for i in range(1, round(math.sqrt(value)+1)) if not value % i) > n:
      break

  return value

def gen():
  num = 1
  while True:
    yield sum(range(num + 1))
    num += 1



##############################################

if __name__ == "__main__":
  cant=500
  
  num = euler_12(cant)
  print(num)

##############################################

"""
76576500
"""
