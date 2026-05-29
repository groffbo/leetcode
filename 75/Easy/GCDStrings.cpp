#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int str1_length = str1.size();
        int str2_length = str2.size();
        int length;

        string substring;

        if(str1_length > str2_length) {
            length = str1_length;
        } else {
            length = str2_length;
        }

        for(int i = 0; i < length; i++) {
            if(str1.substr(0,i) == str2.substr(0, i)) {
                substring = str1.substr(0,i);
            }
        }
    }
};

int main() {
    string str1 = "ABABAB";
    string str2 = "ABAB";
    Solution s;
    s.gcdOfStrings(str1, str2);
}