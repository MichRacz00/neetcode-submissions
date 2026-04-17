class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            current_temp = temperatures[i]
            while stack and temperatures[stack[-1]] <= current_temp:
                stack.pop()
            
            if stack:
                distance = stack[-1] - i
                res[i] = distance
            stack.append(i)

        return res