import heapq

class Solution(object):
    def reorganizeString(self, s):
        #we make a hashmap
        #we put that hashmap into a list of pairs
        #we heapify the hashmap
        #we pop and push the hashmap until the string is done

        freqs = {}
        heap = []

        prev_freq = 0
        prev_char = None

        ret = ""

        for c in s:
            if c in freqs:
                freqs[c] += 1
            else:
                freqs[c] = 1
        
        for char, freq in freqs.items():
            heap.append((-freq, char))

        heapq.heapify(heap)

        while heap:
            freq, char = heapq.heappop(heap)
            ret += char
            freq += 1

            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq, prev_char))

            prev_char = char
            prev_freq = freq

        if len(ret) != len(s):
            return ""

        return ret
