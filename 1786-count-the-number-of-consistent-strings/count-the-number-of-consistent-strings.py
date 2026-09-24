class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        ans = 0
        for word in words:
            is_consistent = True
            for ch in word:
                if ch not in allowed_set:
                    is_consistent = False
                    break

            if is_consistent:
                ans = ans + 1

        return ans

        