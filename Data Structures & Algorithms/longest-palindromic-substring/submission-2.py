class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def checkPalindrome(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            
            return s[l+1:r]
        
        longest = ""

        for i in range(len(s)):
            p1 = checkPalindrome(i, i + 1)
            p2 = checkPalindrome(i, i)

            print(p1, p2)

            longer = p1 if len(p1) > len(p2) else p2

            if len(longer) > len(longest):
                longest = longer

        return longest