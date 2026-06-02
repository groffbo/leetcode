class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        cur=0
        ps = []
        highest = 0

        for i, g in enumerate(gain):
            cur += g
            ps.append(cur)
            highest = max(highest, cur)

        return highest

        