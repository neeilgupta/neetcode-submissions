class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrixRows = len(matrix)
        matrixCols = len(matrix[0])

        l = 0
        r = matrixRows * matrixCols - 1

        while l <= r:
            m = l + ((r - l) // 2)

            rows = m // matrixCols
            cols = m % matrixCols

            if matrix[rows][cols] == target:
                return True
            elif matrix[rows][cols] > target:
                r = m - 1
            else:
                l = m + 1
        return False