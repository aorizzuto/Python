
# Project Euler: 15
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
 _a_    
|_|_|b  2x2
|_|_|
"""

import time

def euler_15(a,b):
  
  seq = []
  for i in range(a):
    seq.append(2+i)

  for i in range(b-1):
    seq[0] = seq[0]+1
    for j in range(1,a):
      seq[j] = seq[j-1]+seq[j]

  return seq[-1]

if __name__ == "__main__":
  a = 20
  b = 20

  start=time.time()
  
  num = euler_15(a,b)
  print("{} x {} = {} paths".format(a,b,num))
  print(time.time()-start,"seg")

"""
20 x 20 = 137846528820 paths
0.0001919269561767578 seg
"""
