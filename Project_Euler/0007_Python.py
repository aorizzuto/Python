
# Project Euler: 7
# What is the 10.001st prime number?

def euler_7(maximo): # Numero máximo de primos
  cont = 0  # Contador de numeros primos
  num = 1   # Contador de numeros
  while True:
    if check_if_prime(num):
      cont += 1 
      print(cont,num)
      if cont == maximo:
        break
    num+=2
  return num

def check_if_prime(num):
  for i in range(num-1,1,-1):
    if num % i == 0:
      return False
  return True

##############################################

if __name__ == "__main__":
  num = 10001
  a = euler_7(num)
  print("El numero primo {} es: {}".format(num,a))
    
##############################################

"""
9985 104593
9986 104597
9987 104623
9988 104639
9989 104651
9990 104659
9991 104677
9992 104681
9993 104683
9994 104693
9995 104701
9996 104707
9997 104711
9998 104717
9999 104723
10000 104729
10001 104743
El numero primo 10001 es: 104743
"""
