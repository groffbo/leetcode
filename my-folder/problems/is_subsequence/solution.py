class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        track_s = 0
        if(len(s) > 0):
            for char in t:
                if(track_s <= len(s) - 1 and s[track_s] == char):
                    track_s += 1
            
            if(track_s == len(s)):
                return True
        else:
            return True # this means that nothing is a subsequence of a string for sure

        return False