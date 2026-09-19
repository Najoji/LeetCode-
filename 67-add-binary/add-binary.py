class Solution(object):
    def addBinary(self, a, b):
        lena = len(a) - 1
        lenb = len(b) - 1
        if a == "0" and b == "0":
            return "0"
        aca = 0
        acb = 0
        sum = 0 
        counta = 0
        countb = 0
        for i in range(lena , -1 , -1):
            if a[i] == "1":
                aca = aca + 2**counta
            counta += 1 
        for j in range(lenb , -1 , -1):
            if b[j] == "1":
                acb = acb + 2**countb
            countb += 1 
        sum = aca + acb
        out = ""
        
        while sum > 0:
            remainder = sum % 2 
            out = str(remainder) + out
            sum = sum//2
        
        return out 
        
        
        