class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def appendToAll(lists: List[List[int]], n: int):
            res = lists[:]
            for l in lists:
                copy = l[:]
                copy.append(n)
                res.append(copy)
            return res
        
        res = [[]]

        for n in nums:
            res = appendToAll(res, n)

        return res