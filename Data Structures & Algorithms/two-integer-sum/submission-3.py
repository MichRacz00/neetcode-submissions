class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        targets = {};
        for i in range(len(nums)):
            n = nums[i];
            if n in targets:
                return [targets[n], i]
            targets[target - n] = i;

        
        