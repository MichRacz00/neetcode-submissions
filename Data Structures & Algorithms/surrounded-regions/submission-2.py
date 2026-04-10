class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        q = deque()

        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                if (x in range(1, len(board) - 1)
                    and y in range(1, len(board[0]) - 1)):
                    continue
                if cell == "O":
                    board[x][y] = "+"
                    q.append((x, y))

        print(board)

        while q:
            x, y = q.popleft()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                newX, newY = dx + x, dy + y

                if newX not in range(0, len(board)):
                    continue
                if newY not in range(0, len(board[0])):
                    continue
                if board[newX][newY] == "X":
                    continue

                print(newX, newY, board[newX][newY])

                if board[newX][newY] == "O":
                    board[newX][newY] = "+"
                    q.append((newX, newY))
        
        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                if cell == "O":
                    board[x][y] = "X"
                if cell == "+":
                    board[x][y] = "O"
        
