class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
            ans = 0
            for s in operations:
                if s[1] == "+":
                    ans += 1
                else:
                    ans -= 1

            return ans