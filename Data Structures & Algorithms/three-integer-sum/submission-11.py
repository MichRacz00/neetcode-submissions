class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            total = n;
            l, r = i + 1, len(nums) - 1

            if i > 0 and n == nums[i - 1]:
                continue

            while l < r:
                curSum = total + nums[l] + nums[r]

                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res
        