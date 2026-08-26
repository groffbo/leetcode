class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # dict where key is the frequency array, and value is the list of words that match that array

        groups = {}

        for s in strs:
            freq = [0] * 26
            for c in s:
                #each character, we add it to that part of the array
                #since a is 0, the ascii for a is 97
                #so the index of each element is 'a' - 97
                index = ord(c) - 97
                #now we just add one to the array spot
                freq[index] += 1
            #now we fully did the word
            key = tuple(freq)
            
            if key in groups:
                groups[key].append(s)
            else:
                val = []
                groups[key] = val
                groups[key].append(s)             
        
        ret = list(groups.values())

        return ret