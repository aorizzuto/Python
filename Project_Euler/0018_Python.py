

# Project Euler: 18
"""
Find the maximum total from top to bottom of the triangle below
"""

import time

def euler_18(pyramid):
  for row in range(len(pyramid) - 1, 0, -1):
      for col in range(len(pyramid[row]) - 1):
          maximum = max(pyramid[row][col], pyramid[row][col + 1])
          pyramid[row - 1][col] += maximum
  return pyramid[0][0]


if __name__ == "__main__":
  a = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

  start=time.time()
  
  num = euler_18(a)
  print("{}".format(num))
  print("\nTiempo de operación:",time.time()-start,"seg")

"""
1074

Tiempo de operación: 0.0002551078796386719 seg
"""
