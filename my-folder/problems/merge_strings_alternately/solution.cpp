class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int p2 = 0;
        int p1 = 0;

        string final;

        while (true) {
            if(p1 != size(word1)) {
                final += word1[p1];
                p1++;
            }

            if(p2 != size(word2)) {
                final += word2[p2];
                p2++;
            }

            if(p2 == size(word2) && p1 == size(word1))
                break;
        }

        return final;
    }
};