class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0

        for n in s:
            count = 0
            num = n
            if (n - 1) not in s:
                while num in s:
                    count += 1
                    num += 1
                if ret < count:
                    ret = count

        return ret