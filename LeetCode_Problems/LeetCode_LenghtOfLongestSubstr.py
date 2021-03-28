"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:  Input: s = "abcabcbb"   Output: 3   Explanation: The answer is "abc", with the length of 3.
Example 2:  Input: s = "bbbbb"      Output: 1   Explanation: The answer is "b", with the length of 1.
Example 3:  Input: s = "pwwkew"     Output: 3   Explanation: The answer is "wke", with the length of 3.
Example 4:  Input: s = ""           Output: 0
"""

import time

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ret = 0

        if len(s) == 1:
            ret = 1

        for first in range(len(s)):
            last_letter = first+1
            
            try:
                while s[last_letter] not in s[first:last_letter]:
                    last_letter+=1
            except:
                pass

            # if len(s[first:last_letter]) > len(longest):
            #     longest=s[first:last_letter]

            ret = max(len(s[first:last_letter]),ret)

        return ret

        


def main():
    sol = Solution()

    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(sol.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(sol.lengthOfLongestSubstring(s))

    s = ""
    print(sol.lengthOfLongestSubstring(s))

    s = " "
    print(sol.lengthOfLongestSubstring(s))

    s = "au"
    print(sol.lengthOfLongestSubstring(s))




if __name__ == '__main__':
    start = time.time()
    main()
    print("\n\nTotal process time: {:.20f} seg.".format(time.time()-start))