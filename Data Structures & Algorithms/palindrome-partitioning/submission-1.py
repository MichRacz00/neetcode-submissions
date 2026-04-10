class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(pal: str):
            l, r = 0, len(pal) - 1
            while l < r:
                if pal[l] != pal[r]:
                    return False
                l += 1
                r -= 1
            return True

        q = deque([(0, [])])
        res = []

        while q:
            i, par = q.popleft()

            if i == len(s):
                res.append(par)
                continue
            
            for j in range(i, len(s)):
                substring = s[i:j+1]
                if isPalindrome(substring):
                    parClone = par[:] + [substring]
                    q.append((j + 1, parClone))
        
        return res