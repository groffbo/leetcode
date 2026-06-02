class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()
        print(x)

        front = 0
        back = len(x) - 1

        while front < back:
            x[front], x[back] = x[back], x[front]
            front += 1
            back -= 1

        s = " ".join(x)

        return s
        