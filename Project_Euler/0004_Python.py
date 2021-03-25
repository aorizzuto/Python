# Project Euler: 4
# Find the largest palindrome made from the product of two 3-digit numbers.

def euler_4(n): # n = n-digit numbers
  maxi = 0
  for i in palin(n):
    if check_palindrome(i):
      maxi = max([maxi,i])
  return maxi

def palin(n):
  for i in range(10**n - 1,1,-1):
    for j in range(10**n - 1,1,-1):
      yield i*j

def check_palindrome(n):
  return str(n)==str(n)[::-1]
    

##############################################

if __name__ == "__main__":
  a = euler_4(3)
  print("Biggest Palindrome = {}".format(a))
    
##############################################

"""
Biggest Palindrome = 906609
"""
