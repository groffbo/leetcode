class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # whenever we hit a non-zero number, we move it to the end of the count index
        # count will be the number of non-zero numbers we've hit so far
        # for example
        #       [0,1,0,3,12]
        # count = 0, traversing hits 1 at index 1
        # we move the number BEFORE increasing the count
        # count = 1, traversing hits 3
        # 3 swaps with whatever is in the 1 index (which is a zero)
        #   [1,0,0,3,12]
        #   [1,3,0,0,12]
        #   [1,3,12,0,0]
        # count = 2, this is a zero so continue without adding
        # we hit 12, since count = 2, we move 

        count = 0
        for i, n in enumerate(nums):
            if(n != 0): 
                nums[i], nums[count] = nums[count], nums[i]
                count += 1
            

        