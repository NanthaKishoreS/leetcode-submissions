class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break

        if index == -1:
            nums.reverse()
            return 

        for i in range(n-1,-1,-1):
            if nums[i]>nums[index]:
                nums[i],nums[index] = nums[index],nums[i]
                break

        i = index+1
        j = n-1
        while j>i:
            nums[i],nums[j] = nums[j],nums[i]
            j = j-1
            i = i+1

        

        