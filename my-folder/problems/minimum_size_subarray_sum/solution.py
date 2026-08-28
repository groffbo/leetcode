class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        minimum = len(nums) + 1
        total = 0

        while right < len(nums):
            total += nums[right]
            while total >= target:
                minimum = min(minimum, (right - left + 1))
                total -= nums[left]
                left += 1

            if total < target:
                right += 1

        if minimum == len(nums) + 1:
            return 0
    
        return minimum 


        #initialize

        #expand

        #shrink

        #update
        