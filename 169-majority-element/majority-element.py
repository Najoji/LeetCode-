class Solution(object):
    def majorityElement(self, nums):
         count = {}
         for i in nums:
            if i in count:
                count[i] = count[i] + 1 
            else:
                count[i] = 1

            if count[i] > len(nums)//2 :
                return i
        
        