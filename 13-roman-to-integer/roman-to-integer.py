class Solution(object):
    def romanToInt(self, s):
        number = 0 
        for i in range(0,len(s)):
            chara = s[i]
            if chara == 'M':
                number = number + 1000
            elif chara == 'D':
                number = number + 500
            elif chara == 'C':
                if i+1 < len(s) and s[i + 1] in ('D' , 'M'):
                    number = number - 100
                else :
                    number = number + 100
            elif chara == 'L':
                number = number + 50
            elif chara == 'X':
                if i+1 < len(s) and s[i + 1] in ('L' , 'C'):
                    number = number - 10
                else :
                    number = number + 10
            elif chara == 'V':
                number = number + 5
            elif chara == 'I':
                if i+1 < len(s) and s[i + 1] in ('V' , 'X'):
                    number = number - 1
                else :
                    number = number + 1
        return number 

     