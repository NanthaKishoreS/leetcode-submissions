class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        largest = max(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                sum = sum + nums[i+1]
            else:
                break
        while sum in nums:
            sum+=1

        return sum 
            