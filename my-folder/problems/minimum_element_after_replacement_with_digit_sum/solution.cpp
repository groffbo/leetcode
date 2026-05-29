#include <vector>
#include <bits/basic_string.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int minElement(vector<int>& nums) {
        // keep track of the minimum number with a tracker
        // add them and then compare to the current lowest

        int minNumIndex = 0;

        for(int i = 0; i < nums.size(); i++) {
            string currentInt = to_string(nums[i]);
            int sum = 0;

            for(int j = 0; j < std::to_string(nums[i]).length(); j++) {
                sum += stoi(currentInt.substr(j, 1));
            }

            nums[i] = sum;
            if(nums[i] < nums[minNumIndex]) {
                minNumIndex = i;
                printf("New min num is: %d", nums[minNumIndex]);
            }
        }
        return nums[minNumIndex];
    }
};

// int main() {

//     Solution s;

//     vector<int> nums = {10, 15, 14, 20};

//     std::cout << s.minElement(nums) << std::endl;

//     return 0;
// }