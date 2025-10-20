class Solution {
public:
    bool isPalindrome(string s) {
        int left = 0;
        int right = size(s) - 1;
        
        while (left < right) {
            if(!isalnum(s[left])) {
                left++;
                continue;
            }

            if(!isalnum(s[right])) {
                right--;
                continue;
            }

            if(tolower(s[right]) != tolower(s[left]))
                return false;

            left++;
            right--;

        }
        return true;
    }
};