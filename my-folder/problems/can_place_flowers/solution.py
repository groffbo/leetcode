class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # flowerbed[i] will either be a 0 or a 1
        # we should just go through the array once, find out ourselves how many flowers can be placed
        # compare if it is greater than the number given
        actual = 0
        ret = False

        for i, f in enumerate(flowerbed):
            # what about for cases where its the border of the array?
            # we'd only need to check one side of it
            # so if the index is 0 or len()-1, just check one side
            if(f == 0 and len(flowerbed) > 1):
                if(i == 0):
                    #only check to the right side
                    if(flowerbed[i+1] == 0):
                        actual += 1
                        flowerbed[i] = 1
                elif(i == len(flowerbed) - 1 and flowerbed[i-1] == 0):
                        actual += 1
                        flowerbed[i] = 1
                elif(flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                        actual += 1
                        flowerbed[i] = 1
            if(len(flowerbed) == 1 and flowerbed[i] == 0):
                    actual += 1   

        if(actual >= n):
            ret = True

        return ret
        