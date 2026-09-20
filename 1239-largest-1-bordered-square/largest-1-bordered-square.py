from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # Separate rows and columns to handle any rectangular matrix
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0
        
        # Initialize prefix matrices with proper rectangular bounds
        rowpref = [[0] * cols for _ in range(rows)]
        colnpref = [[0] * cols for _ in range(rows)]
        
        # 1. Row continuous counts (Left to Right)
        for i in range(rows):
            count = 0
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                rowpref[i][j] = count
                    
        # 2. Column continuous counts (Top to Bottom)
        for j in range(cols):
            count = 0
            for i in range(rows):
                if grid[i][j] == 1:
                    count += 1
                else:
                    count = 0
                colnpref[i][j] = count

        mx = 0
        
        # 3. Evaluate sizes treating (i, j) as the bottom-right corner
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                sz = min(rowpref[i][j], colnpref[i][j])
                
                while sz > 0:
                    # Validate top edge and left edge constraints
                    if rowpref[i - sz + 1][j] >= sz and colnpref[i][j - sz + 1] >= sz:
                        break
                    else:
                        sz -= 1
                        
                mx = max(mx, sz)
                        
        # Return total area (side * side) as requested by this specific variant
        return mx * mx
