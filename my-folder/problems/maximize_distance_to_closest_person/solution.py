class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_dist = 0
        count = 0

        for i, s in enumerate(seats):
            if s == 0:
                count += 1
                if i == len(seats) - 1: #we're at the end of the right side and its a zero
                    max_dist = max(max_dist, count)
            
            if s == 1 and count > 0:
                if i - count == 0: # this means theres no left 1
                    max_dist = max(max_dist, count)
                else:
                    max_dist = max(max_dist, (count + 1) // 2)
                count = 0

        return max_dist
