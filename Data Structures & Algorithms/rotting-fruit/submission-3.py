class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        fresh = 0

        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if cell == 1:
                    fresh += 1
                if cell == 2:
                    q.append((x, y))

        time = 0

        while len(q) > 0 and fresh > 0:
            
            for _ in range(len(q)):
                x, y = q.pop(0)
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dx, dy in directions:
                    newX, newY = dx + x, dy + y
                    
                    if (newX not in range(len(grid))
                        or newY not in range(len(grid[0]))):
                        continue

                    if grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        q.append((newX, newY))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
