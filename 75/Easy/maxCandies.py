class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maximum = max(candies)
        sol = [False] * len(candies)

        for i, candy in enumerate(candies):
            if(candy + extraCandies >= maximum):
                sol[i] = True
        
        return sol
    