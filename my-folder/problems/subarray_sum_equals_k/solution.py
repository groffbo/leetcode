class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # count = 0

        # for i, n in enumerate(nums):
        #     right = i
        #     total = 0
        #     while right < len(nums):
        #         total += nums[right]
        #         right += 1
        #         if total == k:
        #             count += 1

        # return count

        hashmap = {}
        count = 0
        running_sum = 0

        hashmap[0] = 1

        for n in nums:
            running_sum += n
            if (running_sum - k) in hashmap:
                count += hashmap[running_sum - k]

            if running_sum in hashmap:
                hashmap[running_sum] += 1
            else:
                hashmap[running_sum] = 1

        return count
