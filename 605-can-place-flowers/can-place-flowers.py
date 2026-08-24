class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
    
        
        for i in range(len(flowerbed)):
            if  i == 0 and flowerbed[i] == 0 :
                if len(flowerbed) == 1: 
                    n = n - 1
                    flowerbed[i] = 1
                elif flowerbed[i+1] == 0 :
                    flowerbed[i] = 1
                    n = n - 1
            if i != 0 and i != len(flowerbed) - 1 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                n = n - 1
                flowerbed[i] = 1
            if i == len(flowerbed) - 1 and flowerbed[i] == 0:
                if flowerbed[i-1] == 0:
                    n = n - 1
                    flowerbed[i] = 1
        if n <= 0 :
            return True 
        else:
            return False
            


        