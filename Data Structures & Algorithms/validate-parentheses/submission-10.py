class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                stack.append(p)

            if len(stack) == 0:
                return False

            if p == ')' and stack.pop() != '(':
                return False
            elif p == '}' and stack.pop() != '{':
                return False
            elif p == ']' and stack.pop() != '[':
                return False
        return len(stack) == 0
                