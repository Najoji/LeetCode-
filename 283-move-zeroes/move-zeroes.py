class Solution(object):
    def moveZeroes(self, nums):
        insert = 0 
        for i in range(len(nums)) :
            if nums[i] != 0 :
                nums[insert] = nums[i]
                insert = insert + 1 
        for i in range(insert , len(nums)):
            nums[i] = 0 

        
        