class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def bfs(x, y):
            maxSize = 0
            q = [(x, y, 1)]

            while len(q) > 0:
                x, y, size = q.pop(0)
                grid[x][y] = 0
                maxSize = max(size, maxSize)

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for offX, offY in directions:
                    if x + offX not in range(len(grid)):
                        continue
                    if y + offY not in range(len(grid[0])):
                        continue
                    if grid[x + offX][y + offY] == 0:
                        continue

                    size += 1
                    q.append((x + offX, y + offY, size))

            return maxSize

        res = 0
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] == 1:
                    size = bfs(x, y)
                    print(size)
                    res = max(size, res)
        
        return res