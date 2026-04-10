class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphanum(char):
            if ord('a') <= ord(char) <= ord('z'):
                return True
            elif ord('A') <= ord(char) <= ord('Z'):
                return True
            elif ord('0') <= ord(char) <= ord('9'):
                return True
            else:
                return False

        while l < r:
            if not isAlphanum(s[l]):
                l += 1
                continue
            if not isAlphanum(s[r]):
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                print(l, r, s[l], s[r])
                return False
            
            l, r = l + 1, r - 1
        
        return True