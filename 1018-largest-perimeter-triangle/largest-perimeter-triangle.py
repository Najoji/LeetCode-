class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse = True)
        side1 = 0
        side2 = 1
        side3 = 2 
        perimeter = 0 
        for i in range(len(nums)):
            if nums[side1] + nums[side2] > nums[side3] and nums[side2] + nums[side3] > nums[side1] and nums[side1] + nums[side3] > nums[side2]:
                perimeter = nums[side1] + nums[side2] + nums[side3]
                return perimeter
            else :
                if side3 < len(nums) - 1:
                    side1 += 1 
                    side2 += 1
                    side3 += 1
                else :
                    return 0 



            
        