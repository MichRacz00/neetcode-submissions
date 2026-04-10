class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def calcCombs(i, n, k, curComb, combs):
            if len(curComb) == k:
                combs.append(curComb)
                return
            if i > n:
                return

            newComb = curComb.copy()
            newComb.append(i)
            calcCombs(i + 1, n, k, newComb, combs)

            calcCombs(i + 1, n, k, curComb, combs)

        combs = []
        calcCombs(1, n, k, [], combs)

        return combs