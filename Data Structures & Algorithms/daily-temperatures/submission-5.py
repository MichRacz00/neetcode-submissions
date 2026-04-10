class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while stack:
                if temperatures[stack[-1]] <= temperatures[i]:
                    stack.pop()
                else:
                    res[i] = stack[-1] - i
                    break;
            stack.append(i)
        
        return res