class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = None 
        newdiff = 10000000
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1 
            while left < right :
                total = nums[i] + nums[left] + nums[right]
                diff = abs(total - target)
                if diff < newdiff:
                    newdiff = diff
                    closest = total 
                
                if total == target :
                    return total 
                elif total < target :
                    left = left + 1
                else :
                    right = right - 1 
        return closest 


                



        