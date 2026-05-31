#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        //extra candies wont change
        //can store the minimum to beat instead of comparing each iteration
        // find highest number of candies in array once, and then use that value to compare
        int maximum = *max_element(candies.begin(), candies.end());
        vector<bool> ret(candies.size(), false);

        for(int i = 0; i < candies.size(); i++) {
            if(candies[i] + extraCandies >= maximum)
                ret[i] = true;
        }

        return ret;
    }
};

// int main() {
//     Solution s;

//     vector<int> candies = {1, 3, 2, 5, 4};
//     int extraCandies = 3;
//     vector<bool> ret = s.kidsWithCandies(candies, extraCandies);

//     for(int c : ret) {
//         cout << c << endl;
//     }
//     return 0;
// }