class Solution(object):
    def maximumProduct(self, nums):

        nums.sort(reverse = True)
        product = nums[0] * nums[1] * nums[2]
        product1 = nums[0] * nums[-1] * nums[-2] 
        return max(product , product1)
       
        