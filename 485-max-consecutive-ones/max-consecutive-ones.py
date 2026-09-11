class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count = 0 
        maxcon = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1 
                if count > maxcon :
                    maxcon = count 
            else :
                count = 0 
        return maxcon 
        