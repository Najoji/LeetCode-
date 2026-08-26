class Solution(object):
    def pivotIndex(self, nums):
        
        total = 0
        left = 0
        for i in nums:
            total = total + i 
        
        for pivot in range(len(nums)):
            right = total - left - nums[pivot]

            if left == right :
                return pivot 
            left = left + nums[pivot]
        
        return -1 



        