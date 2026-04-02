
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        vector<int> charCount(26, 0);
        for (char c : chars) charCount[c - 'a']++;
        int total = 0;
        for (string& w : words) {
            vector<int> temp = charCount;
            bool good = true;
            for (char c : w) {
                if (--temp[c - 'a'] < 0) {
                    good = false;
                    break;
                }
            }
            if (good) total += w.size();
        }
        return total;
    }
};
