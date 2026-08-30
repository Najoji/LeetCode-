class Solution(object):
    def findMaxAverage(self, nums, k):
        larg = sum(nums[0:k])
        currentlarg = larg
        

        for i in range(k,len(nums)):
            currentlarg = currentlarg - nums[i-k] + nums[i]


        
            if currentlarg > larg :
                larg = currentlarg

        return float(larg) / k  
        

                
