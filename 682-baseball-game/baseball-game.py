class Solution(object):
    def calPoints(self, operations):
        lisp = []
        for i in operations :
            
            if lisp and i == 'C':
                lisp.pop()
            elif lisp and  i == 'D':
                lisp.append(2 * lisp[-1])
            elif lisp and i == '+':
                lisp.append(lisp[-1] + lisp[-2])
            else:
                lisp.append(int(i))
        
        sum = 0 
        for i in lisp:
            sum = sum + i 
        return sum 

        