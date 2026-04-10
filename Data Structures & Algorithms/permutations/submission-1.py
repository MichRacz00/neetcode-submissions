class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, cur):
            if i >= len(nums):
                res.append(cur.copy())
                return

            for split in range(0, len(cur) + 1):
                cur.insert(split, nums[i])
                backtrack(i + 1, cur)
                cur.pop(split)
        
        backtrack(0, [])
        return res