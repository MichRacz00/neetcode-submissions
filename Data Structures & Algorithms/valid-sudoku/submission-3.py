class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_seen = [set() for _ in range(9)]
        col_seen = [set() for _ in range(9)]

        def validateBox(i, j):
            seen = set()
            for i_prime in range(i, i + 3):
                for j_prime in range(j, j + 3):
                    number = board[i_prime][j_prime]
                    if number == ".":
                        continue
                    if number in seen:
                        return False
                    seen.add(number)
            return True

        for i in range(0, 9):
            for j in range(0, 9):
                number = board[i][j]

                if i % 3 == 0 and j % 3 == 0:
                    if not validateBox(i, j):
                        return False

                if number == '.':
                    continue

                if number in row_seen[i]:
                    return False
                if number in col_seen[j]:
                    return False
                
                row_seen[i].add(number)
                col_seen[j].add(number)

        return True
