class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # sliding window technique
        # which means NOT calculating the sum every single time; but only once and adding the new int to it
        window = sum(nums[:k])
        maximum = window

        # how many steps we will have to take len = 6 and k = 4, which means it will be [1,1,1,1,0,0]
        # only 2 steps remaining to take, each time we move the front and back and add/subtract those
        for i in range(len(nums) - k):
            window = ((window - nums[i] + nums[i + k]))
            candidate = window
            if(maximum < candidate):
                maximum = candidate

        return float(maximum) / float(k)