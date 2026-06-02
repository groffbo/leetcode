class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # how to do this in o(n)
        # length of the longest consecutive elements sequence
        # so i guess a hash table, go through the array and sort the hash table
        # once we have the hash table, 
        hashtable = dict()

        for n in nums:
            hashtable.update(n)