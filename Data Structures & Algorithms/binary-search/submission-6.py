class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()

        l, r = 0, len(nums) - 1
        i = 0

        print(nums)

        while l <= r and i < 30:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            
            print(m)
            i += 1

        return -1
        