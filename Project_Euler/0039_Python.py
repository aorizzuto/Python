


# Project Euler: 39
"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

For which value of p <= 1000, is the number of solutions maximised?
"""
"""
- a + b + c = p
- a^2 + b^2 = c^2
- Consideraciones:
    - a,b,c < p
    - a,b < c
    - b <= a  (Porque son intercambiables en la fórmula)
"""

import time
from collections import Counter

def euler_39(lim):
  perimetros = []

  for a in range(1,lim):
    for b in range(1,lim):

      c = (a**2 + b**2)**0.5
      if int(c) == c and (a + b + c) <= lim:

        perimetros.append(a+b+c)
  
  a = Counter(perimetros)

  return a.most_common(1)[0]


##############################################

if __name__ == "__main__":
  
  start = time.time()
  
  lim = 1000

  soluciones = euler_39(lim)

  print("El perimetro mas comun es {} y se repite {} veces".format(soluciones[0],soluciones[1]))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
El perimetro mas comun es 840.0 y se repite 16 veces

Tiempo de operación: 2.8908534049987793 seg
"""


