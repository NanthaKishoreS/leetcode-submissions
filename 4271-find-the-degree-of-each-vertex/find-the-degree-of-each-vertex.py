class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        result = []
        for row in matrix:
            row_size = sum(row)
            result.append(row_size)
        return result

