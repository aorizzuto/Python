# LeetCode_BalancedString.py

import pytest
from LeetCode_BalancedString import Solution

# [Q,W,E,R]
sol = Solution()

def test_1():
    assert sol.balancedString("QWER") == 0      # 0 = [1,1,1,1] max = 1
    assert sol.balancedString("QQWE") == 1      # 1 = [2,1,1,0] max = 1
# s = "QQQR"                  # 2 = [3,0,0,1] max = 1
# print(sol.balancedString(s))
# s = "QQQQ"                  # 3 = [4,0,0,0] max = 1
# print(sol.balancedString(s))
# s = "QWWR"                  # 1 = [1,2,0,1] max = 1
# print(sol.balancedString(s))
# s = "QQEE"                  # 2 = [2,0,2,0] max = 1
# print(sol.balancedString(s))
# s = "WWEQERQWQWWRWWERQWEQ"  # 4 = [5,8,4,3] max = 5
# print(sol.balancedString(s))
# s = "WQWRQQQW"              # 3 = [4,3,0,1] max = 2
# print(sol.balancedString(s))
# s = "WWQQRRRRQRQQ"          # 4 = [5,2,0,5] max = 3
# print(sol.balancedString(s))
