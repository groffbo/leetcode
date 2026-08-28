class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # no prefix sum array
        h = {0:1}
        prefix = 0
        count = 0

        for i, n in enumerate(nums):
            # for each value
            #check if the prefix is already in the hashmap
            prefix += n
            s = prefix - k

            if s in h:
                count += h[s]

            if prefix in h:
                h[prefix] += 1
            else:
                h[prefix] = 1
        
        return count