



# Project Euler: 42
"""
The nth term of the sequence of triangle numbers is given by, tn = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""

import time

def euler_42():

  f = open("p042_words.txt")

  values = []

  for word in f.readlines()[0].replace('"','').split(','):
    values.append(get_value(word))
  
  triangle_numbers = get_triangle_numbers(max(values))

  ret = check_how_many(values,triangle_numbers)

  return ret


def check_how_many(v,tri):
  contador = 0

  for i in v:
    if i in tri:
      contador += 1

  return contador

def get_value(w):
  contador = 0

  for i in w:
    contador += ord(i)-64
  
  return contador


def get_triangle_numbers(lim):
  num = []
  n = 1
  tri = 1
  while tri < lim:
    tri = 1/2*n*(n+1)
    num.append(tri)
    n += 1

  return num


##############################################

if __name__ == "__main__":
  
  start = time.time()

  val = euler_42()

  print("La cantidad de triangle_words es: {}".format(val))


  print("\nTiempo de operación:",time.time()-start, "seg.")
    
##############################################

"""
La cantidad de triangle_words es: 162

Tiempo de operación: 0.012282609939575195 seg.
"""


