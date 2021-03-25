


# Project Euler: 55
"""
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
"""

import time

def euler_55(lim):

  lst = [True]*lim

  for i in range(10,lim):
    if is_palindrome(i):
      lst[i-1] = False

  return len([i for i in lst if i==True]) - 10

  


def is_palindrome(val):
  contador = 0 # Max 50
  done = False
  while True:
    val += int(str(val)[::-1])

    if str(val) == str(val)[::-1]:
      done = True
      break

    contador += 1

    if contador >= 50:
      break

  return done


##############################################

if __name__ == "__main__":

  start=time.time()

  lim = 10000
  a = euler_55(lim)

  print("La cantidad de números Lychrel menores a {} son {}".format(lim,a))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
La cantidad de números Lychrel menores a 10000 son 249

Tiempo de operación: 0.21828913688659668 seg.
"""


