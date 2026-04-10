class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            notAlphanum = False
            if not self.isAlphaNum(s[l]):
                l += 1
                notAlphanum = True
            if not self.isAlphaNum(s[r]):
                r -= 1
                notAlphanum = True
            
            if notAlphanum: continue

            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1

        return True

    def isAlphaNum(self, c: chr):
        return (ord('A') <= ord(c) <= ord('Z') or
               ord('a') <= ord(c) <= ord('z') or
               ord ('0') <= ord(c) <= ord('9'))