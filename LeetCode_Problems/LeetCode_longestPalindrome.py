"""
Given a string s, return the longest palindromic substring in s.

Example 1:  Input: s = "babad"  Output: "bab"   Note: "aba" is also a valid answer.
Example 2:  Input: s = "cbbd"   Output: "bb"
Example 3:  Input: s = "a"      Output: "a"
Example 4:  Input: s = "ac"     Output: "a"
"""

import time

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length=0
        ret = ""

        if len(s) < 2:
            return s[0]

        if len(set(s)) == 1 or s == s[::-1]:
            return s


        for first in range(len(s)):
            last = first + 1
            while last <= len(s):
                st = s[first:last]
                if st == st[::-1] and len(st) > length:
                    length = len(st)
                    ret = st
                    
                last += 1

        return ret

        

        


def main():
    sol = Solution()

    s = "babad"  
    print(sol.longestPalindrome(s))

    s = "cbbd"   
    print(sol.longestPalindrome(s))

    s = "a"
    print(sol.longestPalindrome(s))

    s = "ac"
    print(sol.longestPalindrome(s))

    s = "bb"
    print(sol.longestPalindrome(s))

    s = "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"
    print(sol.longestPalindrome(s))

    s = "vthbaypbzzfrgeqkfsazhvocumiiblrrcxprqhpdkifncwazfrhmimewubfxmgehebepiuhkvghnbtvyckioxavjcezgbpztkimjmugprtwhsbthytmznfdihgtiuogiixshdqhczbkhswgfqfeaxajozaazczvfbnhzgazmcvplwutfdoatytwxpoxyzggjysobgdkurqdocpakcaxzvfcpagipbqfdfwhzitlezfpdhayrroztwgfqmcfkrphzehxbyioqxxvusvhqktmdovrwlijwjdxccylqqhbfbsmmjpgknxpivysnvedjmnasjtaufzdopjmzfubyxcrfqwaulbqnhezmtaygstdtldkqeeeeqkdltdtsgyatmzehnqbluawqfrcxybufzmjpodzfuatjsanmjdevnsyvipxnkgpjmmsbfbhqqlyccxdjwjilwrvodmtkqhvsuvxxqoiybxhezhprkfcmqfgwtzorryahdpfzeltizhwfdfqbpigapcfvzxackapcodqrukdgbosyjggzyxopxwtytaodftuwlpvcmzagzhnbfvzczaazojaxaefqfgwshkbzchqdhsxiigouitghidfnzmtyhtbshwtrpgumjmiktzpbgzecjvaxoikcyvtbnhgvkhuipebehegmxfbuwemimhrfzawcnfikdphqrpxcrrlbiimucovhzasfkqegrfzzbpyabhtv"
    print(sol.longestPalindrome(s))

    s = "bacabab"
    print(sol.longestPalindrome(s))


if __name__ == '__main__':
    start = time.time()
    main()
    print("\n\nTotal process time: {:.20f} seg.".format(time.time()-start))