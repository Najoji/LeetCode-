class Solution(object):
    def thirdMax(self, nums):
        first = -30000000000 
        second = -3000000000 
        third = -30000000000
        for i in nums:
            if i > first :
                first = i 
        for i in nums:
            if i > second and i < first :
                second = i 
        for i in nums :
            if i > third and i < second and i < first :
                third = i 
        
        if third > -30000000000:
            return third 
        else:
            return first 

       
        