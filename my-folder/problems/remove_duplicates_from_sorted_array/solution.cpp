class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int read = 1; // Read array to find unique elements
        int write = 0;
        
        if (nums.empty()) return 0; // Edge case
        
        for (int read; read < size(nums); read++) {
            if (nums[read] != nums[write]) { // Unique value found!
                write++;
                nums[write] = nums[read]; // Now unique value is in its place
            }
        }
        
        return write + 1;
    }
};