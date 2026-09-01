class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        r = [0 for _ in range(rows)]
        c = [0 for _ in range(cols)]

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    r[i] = 1
                    c[j] = 1

        for i in range(rows):
            for j in range(cols):
                if r[i] == 1 or c[j] == 1:
                    matrix[i][j] = 0

        