class Solution:
    def isPalindrome(self, s: str) -> bool:
        pt1 = 0
        pt2 = len(s) - 1

        def isAlphaNum(c):
            if (ord('0') <= ord(c) <= ord('9') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z')):
                return True
            return False

        while (pt1 < pt2):
            while pt1 < pt2 and not isAlphaNum(s[pt1]):
                pt1 += 1
            while pt1 < pt2 and not isAlphaNum(s[pt2]):
                pt2 -= 1

            if(s[pt1].lower() != s[pt2].lower()):
                return False
            pt1 += 1
            pt2 -= 1
        return True
