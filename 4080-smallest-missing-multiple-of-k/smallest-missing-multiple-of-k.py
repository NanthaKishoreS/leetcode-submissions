class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans = set(nums)
        current = k

        while current in nums:
            current += k

        return current
