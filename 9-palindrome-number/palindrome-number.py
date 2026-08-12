class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = str(x)[::-1]
        return rev == str(x)
        