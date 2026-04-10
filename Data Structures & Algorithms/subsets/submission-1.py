class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            for i in range(len(res)):
                subset = res[i]
                subsetIncl = subset[:]
                subsetIncl.append(n)
                res.append(subsetIncl)

        return res