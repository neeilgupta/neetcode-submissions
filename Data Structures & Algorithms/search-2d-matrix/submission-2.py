class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixRows = len(matrix)
        matrixCols = len(matrix[0])

        l = 0
        r = (matrixRows * matrixCols) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            row = m // matrixCols
            col = m % matrixCols

            if (matrix[row][col] == target):
                return True
            elif (matrix[row][col] > target):
                r = m -1
            else:
                l = m + 1
        return False    
