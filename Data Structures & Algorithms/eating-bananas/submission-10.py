class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2

            sumHours = 0
            for countBananas in piles:
                sumHours += math.ceil(countBananas / k)
            
            if h < sumHours:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)
        
        return res
        