class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # assuming that this is a two pointer solution
        new = list(str(x))

        left = 0
        right = len(new) - 1

        while left < right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1

        return True