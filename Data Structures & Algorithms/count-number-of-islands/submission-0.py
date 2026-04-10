class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(x: int, y: int):
            q = [(x, y)]

            while len(q) > 0 and len(q) < 50:
                x, y = q.pop(0)

                if x not in range(len(grid)):
                   continue
                if y not in range(len(grid[0])):
                    continue

                
                
                if grid[x][y] == "1":
                    grid[x][y] = "0"

                    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for offX, offY in directions:
                        q.append((x + offX, y + offY))

        count = 0

        for x, row in enumerate(grid):
            for y, field in enumerate(row):
                if field == "1":
                    count += 1
                    bfs(x, y)
        
        return count