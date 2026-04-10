class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack:
                (lastTemp, index) = stack[-1]
                if lastTemp >= t:
                    break
                stack.pop()
                res[index] = i - index
            stack.append((t, i))

        return res