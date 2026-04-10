class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        inRow = [set() for _ in range(9)]
        inCol = [set() for _ in range(9)]
        inSquare = [[set() for _ in range(3)] for _ in range(3)]


        for y, row in enumerate(board):
            for x, n in enumerate(row):
                if n == '.':
                    continue
                
                if n in inRow[y]:
                    return False
                inRow[y].add(n)

                print(y, inRow[y])

                if n in inCol[x]:
                    return False
                inCol[x].add(n)

                if n in inSquare[x//3][y//3]:
                    return False
                inSquare[x//3][y//3].add(n)
                
        
        return True
