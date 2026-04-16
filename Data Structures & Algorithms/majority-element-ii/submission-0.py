class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        threashold = len(nums) // 3
        cur_count = 1
        res = []
        nums.append(1000000001)

        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                if cur_count > threashold:
                    res.append(nums[i - 1])
                cur_count = 1
            else:
                cur_count += 1
        
        return res

