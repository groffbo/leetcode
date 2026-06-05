class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # maximum water a container can hold is the max height of the smallest of two heights
        # we will proceed forward with the smaller height, check the smallest of the two, that is the amount
        # to get the length, or area, we will take right-left indeces, and then multiply smallest height by the length. save to max if its greater

        # when do we deincrement?
        # we will deincrement the tracker who is SMALLER, and keep the LARGER one

        maxWater = 0
        left = 0 
        right = len(height) - 1

        while(left < right):            
            length = right - left

            if(height[left] > height[right]):
                possibleMax = height[right]
                right -= 1
            else:
                possibleMax = height[left]
                left += 1

            candidate = length * possibleMax

            if(candidate > maxWater):
                maxWater = candidate

        return maxWater
        