class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while j >= i:
            if nums[i] != val:
                i += 1
            elif nums[i] == val:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j -= 1

        return i
