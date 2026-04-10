class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = None
        for n in sorted(nums):
            if prev and prev == n:
                return n
            prev = n
        
        return -1
            