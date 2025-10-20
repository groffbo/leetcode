class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> hash;
        int value;

        for(int i = 0; i < size(nums); i++) {
            hash[nums[i]]++; // Add count
            if (hash[nums[i]] >= ceil((double)size(nums) / 2)) {
                value = nums[i];
            }
        }
        return value;
    }
};