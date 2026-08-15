class Solution(object):
    def plusOne(self, digits):
        length = len(digits)
        power = length - 1 
        number = 0 
        for i in digits:
            number = number + (i * (10**power))
            power = power - 1 
        
        number = number + 1
        digits = []
        for i in str(number):
            digits.append(int(i))

        return digits 
            
        