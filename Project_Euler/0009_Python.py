
# Project Euler: 9
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def euler_9(n): 
  # a+b+c=1000
  # a2+b2=c2

  # Despejando:
  # b = n*(n-2a)/(2*(n-a))
  # c = n - a - b

  a = 1

  for a in range(1,n):
    b = n * (n - 2*a) / (2 * (n - a))
    c = int(n - a - b)
    if b == int(b):
      mul = a*int(b)*c
      return [a,int(b),c],mul


##############################################

if __name__ == "__main__":

  num = 1000

  s,mul = euler_9(num)

  print("El triplet es {}+{}+{}={} y su multiplicacion es:{}".format(s[0],s[1],s[2],num,mul))
    
##############################################

"""
El triplet es 200+375+425=1000 y su multiplicacion es:31875000
"""
