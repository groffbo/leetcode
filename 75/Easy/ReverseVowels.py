class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1

        v = "aeiouAEIOU"

        ans = list(s)

        while(left < right):
            isLeftVowel = v.find(ans[left])
            isRightVowel = v.find(ans[right])
            # if left is a vowel, we stay there
            # if right is also a vowel, we swap them
            if(isLeftVowel != -1 and isRightVowel != -1):
                # this is a vowel for both, so we swap them
                ans[right], ans[left] = ans[left], ans[right]
                right -= 1
                left += 1
            elif(isLeftVowel != -1 and isRightVowel == -1):
                # left is a vowel, right is not. only increment right
                right -= 1
            else:
                #left is not a vowel, right is a vowel
                left += 1

        ans = ''.join(ans)

        return ans
