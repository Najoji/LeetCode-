class Solution(object):
    def isPowerOfTwo(self, n):

        if n == 1:
            return True 
        
        while n > 0 :
            if n % 2 != 0 :
                break
            n = n // 2

        if n == 1:
            return True 

        return False