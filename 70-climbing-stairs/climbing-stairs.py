class Solution(object):
    def climbStairs(self, n):
        one = 1
        two = 2

        for i in range(3,n+1):
            current = one + two 
            one = two 
            two = current 
        
        if n == 1 :
            return 1
        return two 
        
        