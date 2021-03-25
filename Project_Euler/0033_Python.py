


# Project Euler: 33
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""


import time

def euler_33(d):
  start = 10**(d-1)
  fin = 10**d
  n = list(range(start,fin))

  num_final = den_final = 1

  print("Las fracciones son:")

  for num in n:
    for den in n[num-9:]:  # denominador mayor a num
      if check_num_den(num,den):  # Chequeo si comparten un digito
        num_2,den_2 = convert_fraccion(num,den)
        if den_2 != 0 and num_2/den_2 == num/den:
          num_final = num_final*num_2
          den_final = den_final*den_2

          print(f"{num}/{den} = {num_2}/{den_2}")
        
  print(f"      = {num_final}/{den_final}")
  
  a,b = minima_expresion(num_final,den_final)

  print(f"      = {a}/{b}\n")

  return b

def check_num_den(a,b):
  return any([i in str(b) for i in str(a)]) and a%10!=0 and b%10 !=0


def convert_fraccion(a,b):
  if str(a)[0] in str(b):
    if str(a)[0] == str(b)[0]:
      num = str(a)[1]
      den = str(b)[1]
    else:
      num = str(a)[1]
      den = str(b)[0]
  else:
    if str(a)[1] == str(b)[0]:
      num = str(a)[0]
      den = str(b)[1]
    else:
      num = str(a)[0]
      den = str(b)[0]

  return int(num),int(den)


def minima_expresion(a,b):
  div = 2
  while True:
    if a%div == 0 and b%div == 0:
      a/=div
      b/=div
    else:
      div+=1

    if div > 9:
      break
  
  return int(a),int(b)


##############################################

if __name__ == "__main__":

  start=time.time()
  digitos = 2

  c = euler_33(digitos)

  print("El denominador final es: {}".format(c))

  print("\n\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
Las fracciones son:
16/64 = 1/4
19/95 = 1/5
26/65 = 2/5
49/98 = 4/8
      = 8/800
      = 1/100

El denominador final es: 100


Tiempo de operación: 0.01529073715209961 seg.
"""

