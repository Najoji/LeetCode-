class Solution(object):
    def findLHS(self, nums):
        output = 0 
        largoutput = 0 
        dict1 = {}
        for i in nums:
            if i not in dict1 :
                dict1[i] = 1
            else :
                dict1[i] += 1

        for key,value in dict1.items():
            if key + 1 in dict1 :
                output = dict1[key] + dict1[key + 1]
                if output > largoutput:
                    largoutput = output

                
        
        return largoutput

