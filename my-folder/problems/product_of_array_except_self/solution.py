class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix = []
        suffix = [None] * len(nums)

        ans = []

        #find prefix array
        #need to append cur *= next value
        precur = 1
        sufcur = 1
        sufidx = len(nums) - 1

        for n in nums:
            precur *= n #1 * 1, then 1 * 2, then 2 * 3, then 6 * 4
            prefix.append(precur)        # so the final prefix array should be [1,2,6,24]

            sufcur *= nums[sufidx]
            suffix[sufidx] = sufcur
            sufidx -= 1

        # print "prefix: ", prefix
        # print "suffix: ", suffix

        for i, n in enumerate(nums):
            # at the index, the product will be prefix[i-1] * suffix[i+1]
            if(i == 0):
                prod = suffix[1]
                ans.append(prod)
            elif(i == len(nums) - 1):
                prod = prefix[len(nums)-2]
                ans.append(prod)
            else:
                prod = prefix[i-1] * suffix[i+1]
                ans.append(prod)

            #there will be an issue here though. the final products of the beginning
            #and end of the suffix / prefix are already known and given

        return ans
        #find suffix array
        #suffix array is the same but backwards
        #the pattern is the index is all products starting from the back
        #so the index of suffix should be 
        # so for [1,2,3,4]
        # the suffix array is 
        # 4 * 1 = 4, 4 * 3 = 12, 12 * 2 = 24, 24 * 1 = 24 [24,24,12,4]
        # we start from index len(nums) - 1, and decrement backwards


        #prefix array versus suffix array
        #what does that mean?
        #prefix: products of each number and those before it
        #suffix: products of each number and those after it

        #so we have both arrays; what is this telling us about the products?
        # we are specifically looking for the products of all nums except the num itself
        # what we have found is the products up to that num
        # so likely we will have to subtract or divide somewhere?

        #lets take index 2 for example, --3
        # the product of all nums except 3 is 8
        # in our prefix array, we have the product of 1 and 2 at index 1 (before 3)
        # in our suffix array, we have the product of 4 at index 3 (after 3)
        # 2 * 4 = 8, which gives us our final product!

        # so the pattern would be...
        # for prefix, find the product i-1
        # for suffix, find the product i+1
        # IF they exist


        