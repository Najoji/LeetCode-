class Solution(object):
    def thirdMax(self, nums):
        first = None
        second =  None
        third = None
        for i in nums:
            if i > first :
                first = i 
        for i in nums:
            if i > second and i < first :
                second = i 
        for i in nums :
            if i > third and i < second and i < first :
                third = i 
        
        if third is not None:
            return third 
        else:
            return first 

       
        