



# Project Euler: 34
"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
"""
No hay numero de 8 digitos que se pueda expresar de esta forma ya que:
9!*8 = 7-digit number
Es decir que de aquí en adelante ningún valor dará resultado correcto
"""

import time

def euler_34(inf,sup):

  suma = 0
  for num in yield_fact(inf,sup):
    suma += num
  return suma


def sum_fact(n):
  suma = 0
  for dig_index in range(len(n)):  # Cada digito del numero
    fact = 1
    for i in range(1,int(n[dig_index])+1): # Cantidad de veces igual al num
      fact *= i # Factorial
    suma += fact
  
  return suma # Retorno la suma

def yield_fact(inf,sup):
  for num in range(inf,sup):
    if num == sum_fact(str(num)):
      yield num

##############################################

if __name__ == "__main__":

  start=time.time()
  lim_inf = 10
  lim_sup = 2000000 # 9! * 7

  c = euler_34(lim_inf, lim_sup)

  print("La suma de los numeros es: {}".format(c))

  print("\n\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La suma de los numeros es: 40730


Tiempo de operación: 45.31100511550903 seg.
"""


