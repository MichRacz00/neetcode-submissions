class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        q = deque([(0, n, "")])
        res = []

        while q:
            opened, toOpen, pars = q.popleft()
            
            if toOpen < 0 or opened < 0:
                continue

            if toOpen == 0 and opened == 0:
                print(opened, pars)
                res.append(pars)
                continue

            if opened > 0:
                parsClosed = pars[:]
                parsClosed += ")"
                q.append((opened - 1, toOpen, parsClosed))

            parsOpen = pars[:]
            parsOpen += "("
            q.append((opened + 1, toOpen - 1, parsOpen))

        return res