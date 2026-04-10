class Solution:
    def checkValidString(self, s: str) -> bool:
        parStack = []
        starStack = []

        for i, c in enumerate(s):
            if c == "(":
                parStack.append(i)
            elif c == "*":
                starStack.append(i)
            elif c == ")":
                if parStack:
                    parStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False

        while parStack and starStack:
            if parStack.pop() > starStack.pop():
                return False

        return not parStack
