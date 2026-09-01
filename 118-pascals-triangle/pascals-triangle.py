class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1]]
        
        for i in range(1,numRows):
            num = 1
            row = [num]

            for j in range(1,i+1):
                num = num * (i-j+1)
                num = num//j
                row.append(num)
            final.append(row)
        return final
