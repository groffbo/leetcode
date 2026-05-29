#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        int str1_length = str1.size();
        int str2_length = str2.size();

        string larger_string;
        string smaller_string;
        string substring;

        if(str1_length > str2_length) {
            larger_string = str1;
            smaller_string = str2;
        } else {
            larger_string = str2;
            smaller_string = str1;
        }

        for(int i = 1; i < smaller_string.length() + 1; i++) {
             bool isvalid = true;

            if(larger_string.length() % larger_string.substr(0, i).length() == 0 && smaller_string.length() % smaller_string.substr(0,i).length() == 0 && str1.substr(0,i) == str2.substr(0,i)) {
                string candidate = larger_string.substr(0,i);
                //checking the candidate divides evenly into both str1 and str2
                for(int j = 0; j < larger_string.length(); j += candidate.length()) {
                    if(larger_string.substr(j, candidate.length()) != candidate)
                        isvalid = false;
                    if(j < smaller_string.length() && smaller_string.substr(j, candidate.length()) != candidate)
                        isvalid = false;
                }

                if(isvalid)
                    substring = candidate;
            }
        }
        return substring;
    }
};

// int main() {
//     string str1 = "ABABAB";
//     string str2 = "ABAB";
//     Solution s;
//     s.gcdOfStrings(str1, str2);
// }