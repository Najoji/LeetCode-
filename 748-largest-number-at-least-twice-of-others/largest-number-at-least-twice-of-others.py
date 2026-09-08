class Solution(object):
    def dominantIndex(self, nums):
        largest = 0 
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i] 
                index = i 
        
        
        for i in range(len(nums)):
            
            if i == index :
                continue 
            
            if largest < 2 * nums[i] :
                return -1

        return index 
            
        
        
        
       

        