
# Project Euler: 28
"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Se puede ver que los numeros que se suman son:
[1],[3,5,7,9],[13,17,21,25],[31,37,43,49],[57,65,73,81]...
  +2        +4            +6             +8     
"""
import time

def euler_28(n):
  
  number = 1
  cont = 1
  diag = 1

  while True:
    
    for i in range(1,5): # Voy sumando de a 4
      number = number + 2*cont
      diag = diag + number

    cont+=1

    if number >= n**2:
      break
    
  return diag

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 1001 # 5x5

  a = euler_28(number)

  print("La suma de las diagonales es: {}".format(a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La suma de las diagonales es: 669171001

Tiempo de operación: 0.0014324188232421875 seg.
"""
