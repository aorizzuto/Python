

# Project Euler: 22
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

# What is the total of all the name scores in the file?

import time

def euler_22(f): 
  # lines = Lista de nombres
  lines = (f.readlines())[0].replace("\"","").split(',') 
  lines_sorted = sorted(lines)

  lst = []  # Lista de ranking

  for i in range(len(lines_sorted)): # Por cada nombre
    rank = 0
    for j in lines_sorted[i]: # Verifico cada caracter
      rank += ord(j)-64 # 64 = ascii de 'A'
    lst.append(rank*(i+1))

  return sum(lst)


##############################################

if __name__ == "__main__":

  start=time.time()

  f = open("p022_names.txt","r")
  a = euler_22(f)

  print("Suma de los rankings de los nombres del file:\t{}".format(a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Suma de los rankings de los nombres del file:   871198282Tiempo de operación: 0.02399420738220215 seg.
"""

