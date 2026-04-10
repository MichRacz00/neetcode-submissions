class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        visited = [[False]*len(grid[0])]*len(grid)

        def markPath(x: int, y: int, d: int):
            q = [(x, y, d)]

            while len(q) > 0:
                x, y, d = q.pop(0)
                d += 1

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for xOff, yOff in directions:
                    if x + xOff not in range(len(grid)):
                        continue
                    if y + yOff not in range(len(grid[0])):
                        continue
                    if grid[x + xOff][y + yOff] > d:
                        grid[x + xOff][y + yOff] = d
                        q.append((x + xOff, y + yOff, d))


        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 0:
                    markPath(x, y, 0)
                    print()
