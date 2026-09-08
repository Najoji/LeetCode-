class Solution(object):
    def intersect(self, nums1, nums2):
        count = 0 
        result = []
        dict1 = {}
        dict2 = {}
        nums1.sort()
        nums2.sort()
        for i in nums1:
            if i not in dict1:
                dict1[i] = 1 
            else :
                dict1[i] += 1
        for i in nums2:
            if i not in dict2:
                dict2[i] = 1 
            else :
                dict2[i] += 1 
        
        for key in dict1 :
            if key in dict2 :
                count = min(dict1[key] , dict2[key])

                for i in range(count):
                    result.append(key)
        
        return result 

        