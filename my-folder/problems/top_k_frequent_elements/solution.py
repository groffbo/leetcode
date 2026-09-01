import heapq 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # priority queue and then pop from the queue at the end
        # it doesnt matter what the actual count ends up being

        # prio queue with a dict? is that possible?

        #min heap of size k?

        freq = {}
        heap = []
        ret = []


        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        #push using the value, but push the entire object?
        for n in freq:
            print(n)
            heapq.heappush(heap, (-freq[n], n))
        
        #the heap has the highest numbers at the top
        #so we pop the top two and return  
        for n in range(k):
            freq, num = heapq.heappop(heap)
            ret.append(num)

        return ret      