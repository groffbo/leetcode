from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""

        # counts, and frequencies are important
        # so we want to use a hashmap
        # iterate through the hashmap and append it to the string as we go
        counts = Counter(s)

        #we must do items because otherwise we are just iterating the keys
        # the min heap will pick the leftmost / first element to compare against others with 
        maxHeap = [ [-cnt, char] for char, cnt in counts.items() ]

        heapq.heapify(maxHeap)

        prev = None

        while maxHeap or prev:
            #remove the top element from the heap
            if prev and not maxHeap:
                return ""

            cnt, char = heapq.heappop(maxHeap)
            cnt += 1

            ret += char # add to the string

            # now for the prev part
            # since its not part of the hashmap, we store the prev to add it back 

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = [cnt, char] #store the pair
                
        return ret


            

