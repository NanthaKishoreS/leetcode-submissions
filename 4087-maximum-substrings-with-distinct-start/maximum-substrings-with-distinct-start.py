class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = ""
        ans = 0
        for ch in s:
            if ch not in seen:
                ans += 1
                seen = seen+str(ch)

        return ans          