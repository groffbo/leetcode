import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        #add elements to a heap
        #pop k elements from the heap

        heap = []

        for n in nums:
            heapq.heappush(heap, -n)

        for i in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)