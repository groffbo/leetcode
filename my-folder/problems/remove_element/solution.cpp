class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int left = 0;
        int right = size(nums) - 1;

        while (left <= right) {
            if(nums[left] == val) {
                if (nums[right] != val) {
                    nums[left] = nums[right];
                    left++;
                    right--;
                }

                else {
                    right--;
                    continue;
                }
            }

            else {
                left++;
            }
        }
        return left;
    }
};