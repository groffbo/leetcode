class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, n in enumerate(nums):
            candidate = target - n
            if candidate in hashmap:
                return [i, hashmap[candidate]]
            else:
                hashmap[n] = i

        return []