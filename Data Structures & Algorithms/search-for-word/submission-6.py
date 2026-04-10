class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def find(x, y, i):
            if i == len(word):
                return True
                
            if x < 0 or x >= len(board):
                return False
            if y < 0 or y >= len(board[0]):
                return False
            if word[i] != board[x][y]:
                return False
            if (x, y) in visited:
                return False

            visited.add((x, y))
            i += 1

            res = (find(x + 1, y, i) or
                find(x - 1, y, i) or
                find(x, y + 1, i) or
                find(x, y - 1, i))
            
            visited.remove((x, y))

            return res
        
        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                if (find(x, y, 0)):
                    return True
        
        return False