# Project Euler: 14
"""
The following iterative sequence is defined for the set of positive integers:

  n/2 (n is even)
  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

import time, operator

def euler_14(num):
  maximo = 0
  seq = {}

  for n in range(2,num):
    cant = 0
    x = n
    while n != 1:
      if n in seq:
        cant += seq[n]
        break
      else:
        if n%2:
          n = n*3 + 1
        else:
          n /= 2

      cant += 1
    
    seq[x] = cant

    if cant > maximo:
      maximo = cant
      numero = max(seq.items(), key=operator.itemgetter(1))[0]

  return numero, maximo

if __name__ == "__main__":
  num = 1000000

  start=time.time()
  
  number,iteration = euler_14(num)
  print("Number: {}, N° of iterations: {}".format(number,iteration))
  print(time.time()-start,"seg")

"""
Number: 837799, N° of iterations: 524
46.12885332107544 seg
"""

