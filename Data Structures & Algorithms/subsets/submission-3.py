class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            temp_res = res[:]

            for r in temp_res:
                copy_r = r[:]
                copy_r.append(n)
                res.append(copy_r)
        
        return res