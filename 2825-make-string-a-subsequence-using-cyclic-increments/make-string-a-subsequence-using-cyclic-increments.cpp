class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int j = 0, m = str2.size();
        for (char c : str1) {
            if (j < m && (c == str2[j] || (c - 'a' + 1) % 26 + 'a' == str2[j])) j++;
        }
        return j == m;
    }
};
