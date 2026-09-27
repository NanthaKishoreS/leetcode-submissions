class Solution:
    def balancedStringSplit(self, s: str) -> int:
        dummy = 0
        count = 0
        for ch in s:
            if ch=='R':
                dummy += 1
            else:
                dummy -= 1

            if dummy == 0:
                    count += 1
        
        return count
        