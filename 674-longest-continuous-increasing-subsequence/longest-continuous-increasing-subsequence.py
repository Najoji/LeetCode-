class Solution(object):
    def findLengthOfLCIS(self, nums):
        
        if len(nums) == 1:
            return 1
        

        maxi = 0
        i = 1  
 
        while i < len(nums):
            count = 1 
            while i < len(nums) and nums[i] > nums[i-1]: 
                count = count + 1 
                i = i + 1 
            maxi = max(count,maxi)
            i += 1
        return maxi 
        

            

        