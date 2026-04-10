class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        preffix = [0]*len(nums)
        suffix = [0]*len(nums)
        for i in range(len(nums)):
            preffix[i] = prod
            prod = nums[i] * prod
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod = nums[i] * prod
        
        res = [1] * (len(nums))
        for i in range(len(nums)):
            res[i] = preffix[i] * suffix[i]

        return res