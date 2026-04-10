class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        i = 5

        while l <= r:
            m = (l + r) // 2
            print(l, m, r)
            i -= 1

            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l - 1]