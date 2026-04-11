class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quadruples = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    partial_sum = nums[i] + nums[j] + nums[l] + nums[r]

                    if partial_sum < target:
                        l += 1
                    elif partial_sum > target:
                        r -= 1
                    else:
                        new_quadruple = (nums[i], nums[j], nums[l], nums[r])
                        quadruples.add(new_quadruple)
                        l += 1
                        r -= 1
        
        return [list(q) for q in quadruples]