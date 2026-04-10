class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr, nums):
            if not nums:
                return curr
            n = nums.pop()

            newCurr = curr.copy()
            for c in curr:
                newC = c[:]
                newC.append(n)
                newCurr.append(newC)

            return backtrack(newCurr, nums)
        

        return backtrack([[]], nums)
        