


# Project Euler: 36
"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import time

def euler_36(x):
  palin = find_palin(x)
  binary = find_binaries(palin)
  suma = return_sum_palin(binary,palin)
  return suma



def find_palin(maximo):
  palin = []
  for i in range(maximo+1):
    if str(i) == str(i)[::-1]:
      palin.append(i)
  return palin



def find_binaries(palin):
  binary = []

  for i in palin:
    binary.append("{0:b}".format(i))

  return binary



def return_sum_palin(binary,palin):
  final = []
  for i in range(len(binary)):
    if binary[i] == binary[i][::-1] and binary[i][0] != '0':
      final.append(palin[i])
  return sum(final)

##############################################

if __name__ == "__main__":
  
  start = time.time()
  x = 1000000
  
  contador = euler_36(x)

  print("La suma de los palindromos es: {}".format(contador))

  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
La suma de los palindromos es: 872187

Tiempo de operación: 3.204087018966675 seg.
"""

