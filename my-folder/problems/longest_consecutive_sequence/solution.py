class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # the idea is to store into a hashmap and check only one number behind
        # if its consecutive, we're not the first one, so move on

        numbers = set()
        ret = 0

        for n in nums:
            numbers.add(n)

        for n in numbers:
            tmp = 0
            num = n
            if (num - 1) not in numbers:
                while num in numbers:
                    tmp += 1
                    num += 1
            if tmp > ret:
                ret = tmp
        
        return ret
        

                