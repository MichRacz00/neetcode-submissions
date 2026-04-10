class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix) - 1, len(matrix[0]) - 1

        l, r = 0, ROW
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][COL]:
                l, r = 0, COL
                while l <= r:
                    k = (l + r) // 2
                    print(k)

                    if matrix[m][k] == target:
                        return True
                    elif matrix[m][k] > target:
                        r = k - 1
                    elif matrix[m][k] < target:
                        l = k + 1
                print("no")
                return False

            elif matrix[m][COL] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m - 1
        return False