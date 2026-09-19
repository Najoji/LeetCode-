class Solution(object):
    def findTheDifference(self, s, t):
        
        dict1 = {}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1 
            else :
                dict1[s[i]] += 1 
        
        dict2 = {}
        for i in range(len(t)):
            if t[i] not in dict2:
                dict2[t[i]] = 1
            else:
                dict2[t[i]] += 1 
        
        for key,value in dict2.items():
            if dict2[key] != dict1.get(key,0):  
                x = dict2[key] - dict1.get(key,0)
                y = key * x 
        return y 

                
                

        

        