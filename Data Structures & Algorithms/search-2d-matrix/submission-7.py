class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        COL, ROW = len(matrix) - 1, len(matrix[0]) - 1

        def binSearch(target, array):
            l, r = 0, len(array) - 1
            
            while l <= r:
                m = (l + r) // 2
                
                print(array[m], target)
                if target == array[m]:
                    return True
                elif target < array[m]:
                    r = m - 1
                elif target > array[m]:
                    l = m + 1
            return False
        
        l, r = 0, COL
        i = 0
        while l <= r and i < 10:
            m = (l + r) // 2
            
            if matrix[m][0] <= target <= matrix[m][ROW]:
                print("found")
                return binSearch(target, matrix[m])
            elif target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][0]:
                l = m + 1
            i += 1
        return False