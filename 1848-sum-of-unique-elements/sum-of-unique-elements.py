class Solution(object):
    def sumOfUnique(self, nums):
        dict1 = {}
        sum = 0 
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]] = 1 
            else :
                dict1[nums[i]] += 1 

        for keys,values in dict1.items():
            if values == 1 :
                sum = sum + keys 

        return sum 
