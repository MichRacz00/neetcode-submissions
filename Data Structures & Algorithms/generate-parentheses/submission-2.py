class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [""]
        stats = [(n, 0)]
        res = []
        
        while len(stack) > 0:
            pars = stack.pop()
            toOpen, toClose = stats.pop()
            if toOpen == 0 and toClose == 0:
                res.append(pars)
            else:
                if toClose > 0:
                    stack.append(pars + ")")
                    stats.append((toOpen, toClose - 1))

                if toOpen > 0:
                    stack.append(pars + "(")
                    stats.append((toOpen - 1, toClose + 1))
        return res
