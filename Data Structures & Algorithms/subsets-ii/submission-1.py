class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        q = [(0, [])]
        res = []

        for i, n in enumerate(nums):
            while len(q) > 0:

                j, subset = q.pop()

                if j >= len(nums):
                    res.append(subset)
                    continue

                subsetIncl = subset[:]
                subsetIncl.append(nums[j])
                q.append((j + 1, subsetIncl))

                while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                    j += 1
                
                q.append((j + 1, subset))
                

        return res