class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for k in range(len(nums)):
            if k >= 1 and nums[k - 1] == nums[k]:
                continue
            l, r = k + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[k] + nums[l] + nums[r]
                if cur_sum == 0:
                    output.append([nums[k], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        
        return output