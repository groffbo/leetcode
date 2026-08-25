class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #add numbers to hashmap as you go
        #we dont need every instance of the number
        #so the key is just the number

        available = {}
        for i, n in enumerate(nums):
            candidate = target - n

            if candidate in available:
                print(candidate)
                return [i, available[candidate]]

            available[n] = i

        print(available)

        return []