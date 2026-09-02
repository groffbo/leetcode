class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # count = 0

        # for i, n in enumerate(nums):
        #     #at each index
        #     right = i
        #     total = 0
            
        #     while right < len(nums):
        #         total += nums[right]
        #         right += 1
        #         if total == k:
        #             count += 1

        
        # return count

        #optimized solution

        #save off last calculated sum 

        #store ramping sum in list
        
        #key: prefix sum value: count of that prefix sum
        hashmap = {}
        hashmap[0] = 1

        total = 0
        count = 0

        for i, n in enumerate(nums):
            total += n
            if (total - k) in hashmap:
                count += hashmap[total-k]
            if total in hashmap:
                hashmap[total] += 1
            else:
                hashmap[total] = 1

        return count