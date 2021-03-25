

# Project Euler: 43
"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""
"""
Probar generar multiplos de los primos hasta 1000 y verificar que los 3 digitos no estén dentro de esa lista (Ver si baja el tiempo de ejecución)
"""

import time
from itertools import permutations
from collections import Counter

def euler_43():
  s = '0123456789'
  perm = permutations(s)

  lst = []
  values = []

  total = 0

  for i in perm:
    cambiar = True
    
    if i[3] not in '02468':
      cambiar = False
    elif i[5] not in '05':
      cambiar = False
    elif (int(i[2]+i[3]+i[4]))%3 != 0:
      cambiar = False
    elif (int(i[4]+i[5]+i[6]))%7 != 0:
      cambiar = False
    elif (int(i[5]+i[6]+i[7]))%11 != 0:
      cambiar = False
    elif (int(i[6]+i[7]+i[8]))%13 != 0:
      cambiar = False
    elif (int(i[7]+i[8]+i[9]))%17 != 0:
      cambiar = False
    
    if cambiar:
      print(i)
      values.append(int(''.join(i)))

    lst.append(cambiar)


  c = Counter(lst)

  return c[True],sum(values)



##############################################

if __name__ == "__main__":
  
  start = time.time()

  num,val = euler_43()

  print("La cantidad de valores son {} y la suma es {}".format(num,val))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
('1', '4', '0', '6', '3', '5', '7', '2', '8', '9')
('1', '4', '3', '0', '9', '5', '2', '8', '6', '7')
('1', '4', '6', '0', '3', '5', '7', '2', '8', '9')
('4', '1', '0', '6', '3', '5', '7', '2', '8', '9')
('4', '1', '3', '0', '9', '5', '2', '8', '6', '7')
('4', '1', '6', '0', '3', '5', '7', '2', '8', '9')
La cantidad de valores son 6 y la suma es 16695334890

Tiempo de operación: 4.887080192565918 seg.
"""

