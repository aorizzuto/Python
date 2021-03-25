


# Project Euler: 25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

import time

def euler_25(n): 
  cont=2
  for i in gen_fib():
    cont+=1
    if len(str(i)) >= n:
      return i,len(str(i)),cont
  return 0,0,0

def gen_fib():
  a, b = 1,1
  while True:
    a, b = b, a+b
    yield b
  

##############################################

if __name__ == "__main__":

  start=time.time()
  number = 1000

  a,b,c = euler_25(number)

  print("N° index fibonacci number {} (Length:{} digits):\t{}".format(a,b,c))

  print("\nTiempo de operación:",time.time()-start,"seg.")
    
##############################################

"""
N° index fibonacci number 1070066266382758936764980584457396885083683896632151665013235203375314520604694040621889147582489792657804694888177591957484336466672569959512996030461262748092482186144069433051234774442750273781753087579391666192149259186759553966422837148943113074699503439547001985432609723067290192870526447243726117715821825548491120525013201478612965931381792235559657452039506137551467837543229119602129934048260706175397706847068202895486902666185435124521900369480641357447470911707619766945691070098024393439617474103736912503231365532164773697023167755051595173518460579954919410967778373229665796581646513903488154256310184224190259846088000110186255550245493937113651657039447629584714548523425950428582425306083544435428212611008992863795048006894330309773217834864543113205765659868456288616808718693835297350643986297640660000723562917905207051164077614812491885830945940566688339109350944456576357666151619317753792891661581327159616877487983821820492520348473874384736771934512787029218636250627816 (Length:1000 digits):  4782

Tiempo de operación: 0.09739041328430176 seg
"""



