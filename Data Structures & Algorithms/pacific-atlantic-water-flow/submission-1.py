class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def dfs(q):
            visited = set(q)
            while q:
                x, y = q.popleft()
                visited.add((x, y))
            
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                for dx, dy in directions:
                    newX, newY = dx + x, dy + y

                    if (newX < 0 or newX >= len(heights) or
                        newY < 0 or newY >= len(heights[0]) or
                        (newX, newY) in visited):
                        continue

                    if heights[newX][newY] >= heights[x][y]:
                        q.append((newX, newY))

            return visited
        
        pacific = [(x, 0) for x in range(len(heights))]
        pacific += [(0, y) for y in range(len(heights[0]))]

        atlantic = [(x, len(heights[0]) - 1) for x in range(len(heights))]
        atlantic += [(len(heights) - 1, y) for y in range(len(heights[0]))]

        pac = dfs(deque(pacific))
        atl = dfs(deque(atlantic))

        res = []

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if (x, y) in pac and (x, y) in atl:
                    res.append([x, y])

        return res
        
                
