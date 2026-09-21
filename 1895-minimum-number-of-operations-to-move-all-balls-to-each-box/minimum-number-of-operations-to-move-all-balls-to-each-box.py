class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        res = []
        n = len(boxes)
        for i in range(n):
            moves = 0
            for j in range(n):
                if boxes[j] == '1':
                    moves += abs(i-j)
                
            res.append(moves)

        return res                
        