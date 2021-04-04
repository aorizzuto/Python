"""
A valid number can be split up into these components (in order): 
- A decimal number or an integer.
- (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- One of the following formats:
    - At least one digit, followed by a dot '.'.
    - At least one digit, followed by a dot '.', followed by at least one digit.
    - A dot '.', followed by at least one digit.

An integer can be split up into these components (in order):
- (Optional) A sign character (either '+' or '-').
- At least one digit.

For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:  Input: s = "0"  Output: true    
Example 2:  Input: s = "e"  Output: false
Example 3:  Input: s = "."  Output: false
Example 4:  Input: s = ".1" Output: true

Algoritmo:
1) primer char number, sign or dot
2) Luego deben ser numbers o dot si fue signo
3) si encontré un "e", a la derecha debe haber numero
    a la izq debe haber un signo o numero
4) string no debe terminar en dot, "e" o signo
"""

import time
import re

class Solution(object):
    def isNumber(self, x):

        if not self.Check_1_digit(x):
            return False
        if not self.Has_Numbers(x):
            return False
        if not self.Check_e(x):
            return False
        if not self.Check_sign(x):
            return False
        if not self.Check_Dot(x):
            return False
        if not self.Check_letters(x):
            return False
        return True

    def Has_Numbers(self, x):
        return any(char.isdigit() for char in x)

    def Check_letters(self, x):
        if x == []:
            return True
        x = x.upper().replace('E','')
        x = x.upper().replace('+','')
        x = x.upper().replace('-','')
        return not x.lower().islower() # Check if string contains letters

    def Check_1_digit(self,x):
        if len(x) == 1:
            return x.isdigit()
        return True

    def Check_e(self, x):
        valid = True
        if x.upper().count('E') > 1:
            valid = False
        elif x.upper().find('E') != -1:
            left,e,right = x.upper().partition('E')
            valid = self.Check_Left(left) and self.Check_Right(right)
        return valid
    
    def Check_Left(self, left):
        if left == '':
            return False
        return self.isNumber(left)

    def Check_Right(self, right):
        if right == '' or right.find('.') != -1:
            return False
        return self.isNumber(right)

    def Check_sign(self, x):
        if x.upper().find('E') == -1 and sum([x.count('-'),x.count('+')])>1:
            return False
        if x.upper().find('E') != -1:
            return True
        if x.find('+') != -1 or x.find('-') != -1:
            return x[0] in ['+','-']
        return True

    def Check_Dot(self, x):
        x = x.replace('+','')
        x = x.replace('-','')
        x = x.upper().replace('E','')
        try:
            test = float(x)
            return True
        except:
            return False


def main():
    sol = Solution()

    s = "1e5"       # Output: true
    print(sol.isNumber(s))
    s = "145E4"     # Output: true
    print(sol.isNumber(s))
    s = "-45E4"     # Output: true
    print(sol.isNumber(s))
    s = "e"         # Output: false
    print(sol.isNumber(s))
    s = "145E4e"    # Output: false
    print(sol.isNumber(s))
    s = "-45eE4"    # Output: false
    print(sol.isNumber(s))
    s = "-45e"      # Output: false
    print(sol.isNumber(s))
    s = "-e3"      # Output: false
    print(sol.isNumber(s))

    print()

    s = "+2.14" # Output: true
    print(sol.isNumber(s))
    s = "2+.14" # Output: false
    print(sol.isNumber(s))
    s = "-+2.14" # Output: false
    print(sol.isNumber(s))
    s = "2-" # Output: false
    print(sol.isNumber(s))
    s = "-" # Output: false
    print(sol.isNumber(s))

    print()

    s = "."  # Output: false
    print(sol.isNumber(s))
    s = ".1" # Output: true
    print(sol.isNumber(s))
    s = "54.1" # Output: true
    print(sol.isNumber(s))
    s = "541" # Output: true
    print(sol.isNumber(s))
    s = "4." # Output:  true
    print(sol.isNumber(s))
    s = "4.e" # Output:  false
    print(sol.isNumber(s))
    s = "4e." # Output:  false
    print(sol.isNumber(s))

    print()

    s = ".e" # Output:  false
    print(sol.isNumber(s))
    s = "+x45e23"   # Output: false
    print(sol.isNumber(s))   
    s = "6e6.5" # False
    print(sol.isNumber(s))
    s = "6-e6" # False
    print(sol.isNumber(s))
    s = "0"  # Output: true    
    print(sol.isNumber(s))
    s = "+.8"  # Output: true    
    print(sol.isNumber(s))
    s = "005047e+6" # True
    print(sol.isNumber(s))
    s = ".8+" # False
    print(sol.isNumber(s))
    s = "46.e3"
    print(sol.isNumber(s))
    

    

if __name__ == '__main__':
    start = time.time()
    main()
    print("\nTotal process time: {:.20f} seg.".format(time.time()-start))

